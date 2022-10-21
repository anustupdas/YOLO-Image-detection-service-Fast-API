#Please edit the <your-service-name eg. image-detection-service> according to your service name
DEFAULT_CONFIG_PATH = '/etc/image-detection-service/config.yml'
DEFAULT_SERVICE_PORT = 5000
DEFAULT_PROMETHEUS_PORT = 8080
DEFAULT_PROMETHEUS_ENABLED = True
DEFAULT_SILENCE_KLEIN_LOGS = True
DEFAULT_MAX_WORKERS = 4
DEFAULT_LOG_LEVEL = 'info'
DEFAULT_HOST = '0.0.0.0'
PROJECT_NAME = 'example-template-service'
PROJECT_DESCRIPTION = 'Example service of the Media Distillery Service Template'
API_VERSION_PREFIX = '/api/1'

#Please edit the <your-service-name eg. image-detection-service> according to your service name
DEFAULT_YOLO_CLASS_FILE = '/etc/image-detection-service/data/classes/coco.names'
DEFAULT_YOLO_ANNOTATION_FILE = '/etc/image-detection-service/data/dataset/val2017.txt'
DEFAULT_YOLO_ANNOTATION_FILE_TEST = "/etc/image-detection-service/data/dataset/val2017.txt"
DEFAULT_YOLO_DETECTION_PATH = "/etc/image-detection-service/data/detection/"
