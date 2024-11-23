import pytest
from marshmallow import Schema, fields, ValidationError

from app.infrastructure.schemas.validation import ValidationSchema


class MockSchema(Schema):
    name = fields.Str(required=True)


@pytest.fixture
def validation_schema():
    schema = MockSchema()
    return ValidationSchema(schema)


def test_validate_success(validation_schema):
    data = {'name': 'Tatooine'}
    result = validation_schema.validate(data)
    assert result['name'] == 'Tatooine'


def test_validate_failure(validation_schema):
    data = {}
    with pytest.raises(ValidationError):
        validation_schema.validate(data)


def test_serialize(validation_schema):
    data = {'name': 'Tatooine'}
    result = validation_schema.serialize(data)
    assert result['name'] == 'Tatooine'
