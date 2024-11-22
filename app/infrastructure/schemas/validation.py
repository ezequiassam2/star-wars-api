from marshmallow import ValidationError


class ValidationSchema:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        errors = self.schema.validate(data)
        if errors:
            raise ValidationError(errors)
        return self.schema.load(data)

    def serialize(self, data, many=False, host=None):
        self.schema.host = host
        return self.schema.dump(data, many=many)
