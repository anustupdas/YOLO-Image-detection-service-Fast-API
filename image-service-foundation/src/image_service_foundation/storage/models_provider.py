import logging
import os
import pathlib

from image_service_foundation.config.configuration_manager import ConfigurationManager
from image_service_foundation.storage.dropbox_cloud import DropBoxStorage
from image_service_foundation.storage.google_cloud import GoogleStorage

logger = logging.getLogger(__name__)


class ModelsProvider:
    def __init__(self, config: ConfigurationManager, models_converter):
        self.config = config
        self.storage_client_name = self.config.get('storage.client', 'dropbox')
        self._init_client(self.storage_client_name)
        self.enabled_models = self.config.get(
            'models.enabledTypes'
        )  # TODO: move if not os.path.isdir(self.save_path): to model_converter.save_tf()
        self.model_converter = models_converter

        if not self.enabled_models:
            raise ValueError(
                "No models enabled in configuration. "
                "Specify a list of enabled model types with key `models.enabledTypes`."
            )
        self.service_name = self.config.get('storage.serviceName')
        if not self.service_name:
            raise ValueError(
                "No service name specified in configuration. Specify the service name with key storage.serviceName"
            )

        self.destination_folder = self.config.get('models.location', f"/etc/{self.service_name}/models")

    def _init_client(self, storage_client='dropbox'):
        if storage_client == 'gcloud':
            self.storage_client = GoogleStorage(anonymous=True)
        elif storage_client == 'dropbox':
            self.storage_client = DropBoxStorage(self.config['dropbox.accesstoken'])
        else:
            raise NotImplementedError('Currently only supported for gcloud & dropbox')
        logger.info(f"Initialized ModelsProvider with storage client {storage_client}")

    def _get_file_destination(self, model_type, filename):
        destination_folder = os.path.join(self.destination_folder, model_type)
        destination_path = os.path.join(destination_folder, os.path.basename(filename))
        return destination_path

    def download_models(self):
        for model_type in self.enabled_models:
            logger.info(f"Attempting download of {model_type}")
            try:
                blob_name = self.config.data[f'{model_type}.modelName']
            except KeyError:
                raise ValueError(f"No configuration value found for `{model_type}.modelName`.")

            file_destination = self._get_file_destination(model_type, blob_name)
            folder_destination = os.path.dirname(os.path.abspath(file_destination))
            os.makedirs(folder_destination, exist_ok=True)

            file_destination = pathlib.Path(file_destination)
            if not file_destination.exists() or file_destination.stat().st_size == 0:
                bucket_name = self.config.get('storage.bucket', 'md-data-bingemarkers')
                self.storage_client.download(bucket_name, blob_name, file_destination)

            self.model_converter.save_tf()
