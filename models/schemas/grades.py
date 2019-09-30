from marshmallow import Schema, fields


class Grade:
    def __init__(self, grade_id, date, grade):
        self.grade_id = grade_id
        self.date = date
        self.grade = grade


class GradeSchema(Schema):
    grade_id = fields.Str()
    date = fields.DateTime()
    grade = fields.Int()
