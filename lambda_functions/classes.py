import json
import logging.config

from pynamodb.exceptions import DoesNotExist

import utils.http_responses as api_responses
from models import classy as model


SCHOOLIO = 'schoolio'

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info(event)
    if event['resource'] == '/classes' and event['httpMethod'] == 'POST' and is_valid_create(json.loads(event['body'])):
        request_payload = json.loads(event['body'])
        schoolio_class = model.Class(name=request_payload['name']).save()
        return api_responses.http_201_response(response_body_dict=schoolio_class)
    elif event['resource'] == '/classes' and event['httpMethod'] == 'PATCH' and is_valid_update(
            json.loads(event['body'])):
        request_payload = json.loads(event['body'])
        schoolio_class = model.Class(class_id=request_payload['class_id'], name=request_payload['name']).update()
        return api_responses.http_200_response(response_body_dict=schoolio_class)
    elif event['resource'] == '/classes/{class_id}' and event['httpMethod'] == 'GET':
        return handle_get_method(event)
    else:
        return api_responses.http_400_response(response_body_dict={'message': 'Please submit valid request'})


def handle_get_method(event):
    class_id = event['pathParameters']['class_id']
    try:
        schoolio_class = model.Class.get_class_by_id(class_id)
        return api_responses.http_200_response(response_body_dict=schoolio_class)
    except DoesNotExist:
        return api_responses.http_404_response()
    except:
        return api_responses.http_400_response(response_body_dict={'message': 'Please submit valid request'})


def is_valid_create(request_payload):
    return request_payload.get('name') and len(request_payload) == 1


def is_valid_update(request_payload):
    return request_payload.get('name') and request_payload.get('class_id') and len(request_payload) == 2
