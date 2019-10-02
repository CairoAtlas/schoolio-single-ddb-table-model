import json
import logging.config
import uuid

from models.schoolio import Schoolio
from schemas.classes import Class, ClassSchema

SCHOOLIO = 'schoolio'

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info(event)
    body = json.loads(event['body'])
    class_id = f'class_{str(uuid.uuid4())}'
    class_obj = Class(class_id, body['name'])
    class_schema = ClassSchema(only=('name', 'pk', 'sk'))
    class_schema.context = {
        'pk': f'{SCHOOLIO}_{class_id}',
        'sk': class_id
    }

    class_schema_dict = class_schema.dump(class_obj)

    schoolio_class_record = Schoolio(class_schema_dict.pop('pk'), class_schema_dict.pop('sk'), **class_schema_dict)

    LOGGER.info(schoolio_class_record)
    schoolio_class_record.save()

    return {
        'statusCode': 201,
        'body': json.dumps({
            'class_id': class_id,
            'name:': body['name']
        })
    }



