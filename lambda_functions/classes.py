import json
import logging.config
from models import classy as model

SCHOOLIO = 'schoolio'

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info(event)
    if event['resource'] == '/classes' and event['httpMethod'] == 'POST' and is_valid_create(json.loads(event['body'])):
        request_payload = json.loads(event['body'])
        return {
            'statusCode': 201,
            'body': json.dumps(model.Class(request_payload['name']).save())
        }
    elif event['resource'] == '/classes/{class_id}' and event['httpMethod'] == 'GET':
        class_id = event['pathParameters']['class_id']
        return {
            'statusCode': 200,
            'body': json.dumps(model.Class.get_class_by_id(class_id))
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Please submit valid request'})
        }


def is_valid_create(request_payload):
    return request_payload.get('name') and len(request_payload) == 1
