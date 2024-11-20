from marshmallow import Schema, fields

class FilmSchema(Schema):
    title = fields.Str(required=True)
    release_date = fields.Date(required=True)
    director = fields.Str(required=True)
    planets = fields.List(fields.Str(), required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()