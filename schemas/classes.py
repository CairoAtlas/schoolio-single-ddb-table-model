from marshmallow import Schema, fields


class Class:
    def __init__(self, class_id, name):
        self.class_id = class_id
        self.name = name


class ClassSchema(Schema):
    class_id = fields.Str(load_only=True)
    name = fields.Str(required=True)
    pk = fields.Method('build_pk')
    sk = fields.Method('build_sk')
    data = fields.Method('build_data')

    def build_pk(self, class_obj):
        return self.context.get("pk")

    def build_sk(self, class_obj):
        return self.context.get("sk")

    def build_data(self, class_obj):
        return self.context.get('data')
