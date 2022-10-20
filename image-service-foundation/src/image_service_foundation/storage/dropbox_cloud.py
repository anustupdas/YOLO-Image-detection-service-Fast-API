import pathlib
import dropbox
from dropbox.exceptions import AuthError


class DropBoxStorage:
    def __init__(self, config) -> None:
        self.accesstoken = config.get('dropbox.accesstoken', 'sl.BReA534YoYVlzYVyMpS-IfVtmtF9epPBOtHX1b1qbUz7heu-wH7arT7Fm1UZ0VD2FobvrE-hrk2zOYwhGrPgydMK1uX5s_zwMuDqPWaiE0eKhtuVu7ND82f44j0ZeV_jNZZ-UWE5YT4N')
        self.dropbox_file_path = config.get('dropbox.dropbox_file_path', '/Apps/Yolo4_demo_test/yolov4.weights')

    def _dropbox_connect(self):
        """Create a connection to Dropbox."""
        try:
            dbx = dropbox.Dropbox(self.accesstoken)
        except AuthError as e:
            print('Error connecting to Dropbox with access token: ' + str(e))
        return dbx

    def download(self, local_file_path)-> None:
        try:
            dbx = self._dropbox_connect()

            with open(local_file_path, 'wb') as f:
                metadata, result = dbx.files_download(path=self.dropbox_file_path)
                f.write(result.content)
        except Exception as e:
            print('Error downloading file from Dropbox: ' + str(e))

