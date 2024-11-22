from marshmallow import Schema, fields

from app.infrastructure.utils import DATETIME_FORMAT


class PlanetSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    climate = fields.Str(required=True)
    terrain = fields.Str(required=True)
    film = fields.Str(required=True)
    created_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)
    updated_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)
