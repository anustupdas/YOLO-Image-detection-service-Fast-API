import pathlib
import typing

import dropbox


class DropBoxStorage:
    def __init__(self, accesstoken: str) -> None:
        self.accesstoken = accesstoken

    def download(
        self, bucket_name: str, blob_name: typing.Union[str, pathlib.Path], filepath: typing.Union[str, pathlib.Path]
    ) -> None:
        connection = dropbox.Dropbox(self.accesstoken)
        with connection:
            with open(filepath, 'wb') as f:
                metadata, result = connection.files_download(path=str(blob_name))
                f.write(result.content)
