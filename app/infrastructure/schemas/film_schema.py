from marshmallow import Schema, fields

from app.infrastructure.utils import DATETIME_FORMAT


class FilmSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    release_date = fields.DateTime(format='%Y-%m-%d', required=True)
    director = fields.Str(required=True)
    planets = fields.List(fields.Str(), required=True)
    created_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)
    updated_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)
