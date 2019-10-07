import json
import logging.config

from pynamodb.exceptions import DoesNotExist

import utils.http_responses as api_responses
from models import students as student_model

SCHOOLIO = 'schoolio'

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info(event)
    if event['resource'] == '/students' and event['httpMethod'] == 'POST':
        return handle_post_method(event)
    elif event['resource'] == '/students' and event['httpMethod'] == 'PATCH' and is_valid_update(
            json.loads(event['body'])):
        request_payload = json.loads(event['body'])
        # schoolio_class = student_model.Class(class_id=request_payload['class_id'],
        #                                      name=request_payload['name']).update()
        return api_responses.http_200_response(response_body_dict=schoolio_class)
    elif event['resource'] == '/students/{student_id}' and event['httpMethod'] == 'GET':
        return handle_get_method(event)
    else:
        return api_responses.http_400_response(response_body_dict={'message': 'Please submit valid request'})


def handle_post_method(event):
    try:
        request_payload = json.loads(event['body'])
        schoolio_class = student_model.Student(first_name=request_payload['first_name'],
                                               last_name=request_payload['last_name'],
                                               class_id=request_payload['class_id']).save()
        return api_responses.http_201_response(response_body_dict=schoolio_class)
    except ValueError:
        LOGGER.warning(f'Value Error for {event["body"]}')
        return api_responses.http_400_response(response_body_dict={'message': 'Please submit valid request'})
    except DoesNotExist:
        LOGGER.warning(f'Class does not exist {event["body"]}')
        return api_responses.http_400_response(
            response_body_dict={'message': 'Class does not exist. Please submit valid request'})
    except:
        return api_responses.http_500_response()


def handle_get_method(event):
    student_id = event['pathParameters']['student_id']
    try:
        schoolio_class = student_model.Student.get_student_by_id(student_id)
        return api_responses.http_200_response(response_body_dict=schoolio_class)
    except DoesNotExist:
        return api_responses.http_404_response()
    except:
        return api_responses.http_400_response(response_body_dict={'message': 'Please submit valid request'})


def is_valid_update(request_payload):
    return request_payload.get('name') and request_payload.get('class_id') and len(request_payload) == 2
