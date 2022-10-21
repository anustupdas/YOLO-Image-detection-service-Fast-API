import logging
from typing import Optional

import numpy as np
from image_detection_core.service.object_detection_service import ObjectDetectionService
from image_detection_core.utils import check_number_input
from image_service_foundation.config.configuration_manager import (
    ConfigurationManager,
    ConfigurationMixin,
)

from image_detection_service.constants import *
from image_detection_service.version import __version__

logger = logging.getLogger(__name__)

__all__ = ('DlImageAnalysisService',)


class DlImageAnalysisService(ConfigurationMixin):
    def __init__(self, config: ConfigurationManager = None) -> None:
        self.load_config(config=config, default_location=DEFAULT_CONFIG_PATH)
        self.object_detection_service = ObjectDetectionService(config=config)

    def add(self, data) -> float:
        sum = 0
        print(data)
        print(f"We have {check_number_input(data)} numbers to add")
        for i in data:
            sum += i
            print(sum)

        print(f"Version of the service: {__version__}")
        return sum

    def version(self) -> float:
        print(f"Version of the service: {__version__}")
        v = __version__
        return v

    def detect(self, image: np.ndarray, allowed_classes: str = None, metadata: Optional[dict] = None):
        detections = self.object_detection_service.detect(image, allowed_classes=allowed_classes)
        return detections
