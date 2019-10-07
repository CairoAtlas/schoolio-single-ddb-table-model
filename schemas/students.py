from marshmallow import Schema, fields


class Student:
    def __init__(self, student_id, class_id, first_name=None, last_name=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.class_id = class_id


class StudentSchema(Schema):
    student_id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    class_id = fields.Str()
    pk = fields.Method('build_pk')
    sk = fields.Method('build_sk')
    data = fields.Method('build_data')

    def build_pk(self, class_obj):
        return self.context.get("pk")

    def build_sk(self, class_obj):
        return self.context.get("sk")

    def build_data(self, class_obj):
        return self.context.get('data')
