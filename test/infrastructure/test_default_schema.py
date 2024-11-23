import pytest
from marshmallow import fields

from app.infrastructure.schemas.default_schema import DefaultSchema


class MockSchema(DefaultSchema):
    name = fields.Str(required=True)


@pytest.fixture
def default_schema():
    return MockSchema()


def test_transform_ids_to_urls(default_schema):
    data = {'id': 1, 'name': 'Tatooine'}
    default_schema.host = 'http://test.com'
    default_schema.base_path = 'planets'
    default_schema.depends_on = None
    result = default_schema.dump(data)
    assert result['url'] == 'http://test.com/planets/1'
