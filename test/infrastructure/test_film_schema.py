from datetime import datetime

import pytest

from app.infrastructure.schemas.film_schema import FilmSchema


@pytest.fixture
def film_schema():
    return FilmSchema()


def test_film_schema_load(film_schema):
    data = {
        'title': 'A New Hope',
        'release_date': '1977-05-25',
        'director': 'George Lucas',
        'planets': [1, 2, 3]
    }
    result = film_schema.load(data)
    assert result['title'] == 'A New Hope'


def test_film_schema_dump(film_schema):
    data = {
        'id': 1,
        'title': 'A New Hope',
        'release_date': datetime.strptime('1980-05-21', "%Y-%m-%d"),
        'director': 'George Lucas',
        'planets': [1, 2, 3]
    }
    film_schema.host = 'http://test.com'
    result = film_schema.dump(data)
    assert result['url'] == 'http://test.com/films/1'
