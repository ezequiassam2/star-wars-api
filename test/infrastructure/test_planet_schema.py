import pytest

from app.infrastructure.schemas.planet_schema import PlanetSchema


@pytest.fixture
def planet_schema():
    return PlanetSchema()


def test_planet_schema_load(planet_schema):
    data = {
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'film': 'A New Hope'
    }
    result = planet_schema.load(data)
    assert result['name'] == 'Tatooine'


def test_planet_schema_dump(planet_schema):
    data = {
        'id': 1,
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'film': 'A New Hope'
    }
    planet_schema.host = 'http://test.com'
    result = planet_schema.dump(data)
    assert result['url'] == 'http://test.com/planets/1'
