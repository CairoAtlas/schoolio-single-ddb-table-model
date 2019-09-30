from marshmallow import Schema, fields


class Class:
    def __init__(self, class_id, name):
        self.class_id = class_id
        self.title = name


class ClassSchema(Schema):
    class_id = fields.Str()
    name = fields.Str()
