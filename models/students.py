import uuid

from schemas import students as student_schema
from models import classy as class_model
from models.single_table.schoolio import Schoolio

SCHOOLIO = 'schoolio'


class Student:
    def __init__(self,
                 student_id=f'student_{str(uuid.uuid4())}',
                 first_name=None,
                 last_name=None,
                 class_id=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{first_name} {last_name}'
        self.class_id = class_id

    def save(self):
        if not self.first_name or not self.last_name or not self.class_id:
            raise ValueError('Missing student properties')
        self._make_student_schoolio_object(self.student_id,
                                           self.first_name,
                                           self.last_name,
                                           self.class_id,
                                           self.full_name).save()
        class_item = class_model.Class.get_class_by_id(self.class_id)
        self._make_student_class_schoolio_object(
                self.student_id,
                self.class_id,
                class_item['data']).save()
        return student_schema.Student(self.student_id, self.first_name, self.last_name, self.class_id).__dict__

    def update(self):
        items_to_update = self._get_students_to_update_by_name()
        for item in items_to_update:
            item.update(actions=[
                Schoolio.data.set(self.full_name)
            ])

        return student_schema.Student(self.student_id, self.first_name, self.last_name, self.class_id).__dict__

    def _get_students_to_update_by_name(self):
        items = list()
        results = Schoolio.data_index.query(self.full_name)
        last_evaluated_key = results.last_evaluated_key
        for item in results:
            items.append(item)

        while last_evaluated_key:
            results = Schoolio.data_index.query(self.full_name,
                                                last_evaluated_key=last_evaluated_key)
            last_evaluated_key = results.last_evaluated_key
            for item in results:
                items.append(item)

        return items

    @staticmethod
    def get_student_by_id(student_id):
        schoolio_student_record = Schoolio.get(f'{SCHOOLIO}_{student_id}', student_id)
        return student_schema.Student(schoolio_student_record.sk,
                                      schoolio_student_record.first_name,
                                      schoolio_student_record.last_name,
                                      schoolio_student_record.class_id).__dict__

    @staticmethod
    def _make_student_schoolio_object(
            student_id,
            first_name,
            last_name,
            class_id,
            full_name):
        student_schema_dict = Student._make_student_schema_dict(student_id, first_name, last_name, class_id, full_name)
        schoolio_class_record = Schoolio(student_schema_dict.pop('pk'), student_schema_dict.pop('sk'),
                                         **student_schema_dict)
        return schoolio_class_record

    @staticmethod
    def _make_student_class_schoolio_object(
            student_id,
            class_id,
            class_name):
        student_schema_dict = Student._make_student_class_schema_dict(student_id, class_id, class_name)
        schoolio_class_record = Schoolio(student_schema_dict.pop('pk'), student_schema_dict.pop('sk'),
                                         **student_schema_dict)
        return schoolio_class_record

    @staticmethod
    def _make_student_schema_dict(student_id, first_name, last_name, class_id, full_name):
        student_obj = student_schema.Student(student_id, class_id, first_name=first_name, last_name=last_name)
        student_schema_obj = student_schema.StudentSchema(
            only=('pk', 'sk', 'data', 'first_name', 'last_name', 'class_id'))
        student_schema_obj.context = {
            'pk': f'{SCHOOLIO}_{student_id}',
            'sk': student_id,
            'data': full_name
        }
        return student_schema_obj.dump(student_obj)

    @staticmethod
    def _make_student_class_schema_dict(student_id,
                                        class_id,
                                        class_name):
        student_obj = student_schema.Student(student_id, class_id)
        student_schema_obj = student_schema.StudentSchema(
            only=('pk', 'sk', 'data', 'class_id'))
        student_schema_obj.context = {
            'pk': f'{SCHOOLIO}_{student_id}',
            'sk': class_id,
            'data': class_name
        }
        return student_schema_obj.dump(student_obj)
