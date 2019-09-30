from marshmallow import Schema, fields


class Teacher:
    def __init__(self, teacher_id, first_name, last_name):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name


class TeacherSchema(Schema):
    teacher_id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
