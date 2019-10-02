import json
import logging.config
from models import classy as model

SCHOOLIO = 'schoolio'

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info(event)
    body = json.loads(event['body'])
    schoolio_class = model.Class(body['name'])

    LOGGER.info(schoolio_class)
    schoolio_class.save()

    return {
        'statusCode': 201,
        'body': json.dumps(schoolio_class.save())
    }



