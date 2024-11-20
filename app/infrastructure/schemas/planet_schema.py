from marshmallow import Schema, fields

class PlanetSchema(Schema):
    name = fields.Str(required=True)
    climate = fields.Str(required=True)
    diameter = fields.Int(required=True)
    population = fields.Int(required=True)
    films = fields.List(fields.Str(), required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
