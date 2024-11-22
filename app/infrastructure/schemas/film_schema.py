from marshmallow import Schema, fields

class FilmSchema(Schema):
    title = fields.Str(required=True)
    release_date = fields.DateTime(format='%Y-%m-%d', required=True)
    director = fields.Str(required=True)
    planets = fields.List(fields.Str(), required=True)
    created_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S', dump_only=True)
    updated_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S', dump_only=True)