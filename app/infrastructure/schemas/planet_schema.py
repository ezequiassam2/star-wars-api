from marshmallow import fields

from app.infrastructure.schemas.default_schema import DefaultSchema


class PlanetSchema(DefaultSchema):
    name = fields.Str(required=True)
    climate = fields.Str(required=True)
    terrain = fields.Str(required=True)
    film = fields.Str(required=True)

    def __init__(self):
        super().__init__()
        self.base_path = 'planets'
        self.depends_on = None
