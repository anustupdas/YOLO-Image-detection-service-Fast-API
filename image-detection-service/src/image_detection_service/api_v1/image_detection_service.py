import logging
from typing import List

import numpy as np
from fastapi import APIRouter, File, Request

from image_detection_service.metrics import metrics
from image_detection_service.service import DlImageAnalysisService
from image_detection_service.utils import initialize_configuration

logger = logging.getLogger(__name__)


__all__ = ('example_service_router',)

service: DlImageAnalysisService


def on_startup() -> None:
    """Lazy loading of the service to avoid loading models too soon."""
    global service
    config = initialize_configuration()
    service = DlImageAnalysisService(config=config)


example_service_router = APIRouter()
example_service_router.add_event_handler('startup', on_startup)


@example_service_router.post('/example/sum', tags=['sum'])
async def addition(inputs: List[float]):

    logger.info(f'Received addition request (service)')
    metrics.called('/example/sum')
    try:
        response = service.add(data=inputs)
    except Exception:
        metrics.call_failed('/example/sum')
        raise

    logger.debug(f"Returning response {response}")

    return response


@example_service_router.post('/example/detect', tags=['detect'])
def detect(
    request: Request, classes_to_detect: str = None, frame: bytes = File(..., description='An arbitrary image.')
) -> dict:
    try:
        metadata = request.query_params.__dict__['_dict']
    except Exception:
        metadata = {}

    try:
        image = np.fromstring(frame, np.uint8)
        response = service.detect(image, allowed_classes=classes_to_detect, metadata=metadata)
    except Exception as e:

        logger.error('Request failed.', str(e))
        raise

    logger.info(f'Returning response: {response}')
    return response


@example_service_router.get('/example/version', tags=['version'])
async def version():

    logger.info(f'Received addition request (service)')
    metrics.called('/example/version')
    try:
        response = service.version()
    except Exception:
        metrics.call_failed('/example/version')
        raise

    logger.debug(f"Returning response {response}")

    return response
