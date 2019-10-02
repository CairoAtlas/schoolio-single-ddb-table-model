import uuid

from schemas import classes as schema
from models.single_table.schoolio import Schoolio


SCHOOLIO = 'schoolio'


class Class:
    def __init__(self, name, class_id=f'class_{str(uuid.uuid4())}'):
        class_obj = schema.Class(class_id, name)
        class_schema = schema.ClassSchema(only=('name', 'pk', 'sk'))
        class_schema.context = {
            'pk': f'{SCHOOLIO}_{class_id}',
            'sk': class_id
        }

        class_schema_dict = class_schema.dump(class_obj)

        schoolio_class_record = Schoolio(class_schema_dict.pop('pk'), class_schema_dict.pop('sk'), **class_schema_dict)

        self.class_id = class_id
        self.name = name
        self.schoolio_class_record = schoolio_class_record

    def save(self):
        self.schoolio_class_record.save()
        return schema.Class(self.class_id, self.name).__dict__
