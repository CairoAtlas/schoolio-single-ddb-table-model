from marshmallow import Schema, fields


class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name


class StudentSchema(Schema):
    student_id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
