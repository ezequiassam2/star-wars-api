from marshmallow import fields

from app.infrastructure.schemas.default_schema import DefaultSchema


class FilmSchema(DefaultSchema):
    title = fields.Str(required=True)
    release_date = fields.DateTime(format='%Y-%m-%d', required=True)
    director = fields.Str(required=True)
    planets = fields.List(fields.Int(), required=True)

    def __init__(self):
        super().__init__()
        self.base_path = 'films'
        self.depends_on = 'planets'
