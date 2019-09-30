from marshmallow import Schema, fields


class Subject:
    def __init__(self, subject_id, title):
        self.subject_id = subject_id
        self.title = title


class SubjectSchema(Schema):
    subject_id = fields.Str()
    title = fields.Str()
