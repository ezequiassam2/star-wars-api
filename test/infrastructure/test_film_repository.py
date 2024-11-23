from unittest.mock import MagicMock

import pytest

from app.domain.exceptions import PlanetNotFoundException
from app.domain.models.film import Film
from app.infrastructure.repositories.film_repository import FilmRepository


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.film_repository.FilmRepository.db', mock_db)
    monkeypatch.setattr('app.infrastructure.repositories.film_repository.FilmRepository.collection', mock_db)
    return mock_db


@pytest.fixture
def film_repository():
    return FilmRepository()


def test_save_film(film_repository):
    film = Film(id=None, title='A New Hope', release_date='1977-05-25', director='George Lucas', planets=[1, 2, 3])
    film_repository.db.planets.find_one.return_value = True
    film_repository.get_next_sequence = MagicMock(return_value=1)
    film_repository.save(film)
    film_repository.collection.update_one.assert_called_once()


def test_save_film_raises_exception(film_repository):
    film = Film(id=None, title='A New Hope', release_date='1977-05-25', director='George Lucas', planets=[1, 2, 3])
    film_repository.db.planets.find_one.return_value = None
    with pytest.raises(PlanetNotFoundException):
        film_repository.save(film)


def test_get_all_films(film_repository):
    film_repository.collection.find.return_value = [
        {'id': 1, 'title': 'A New Hope', 'release_date': '1977-05-25', 'director': 'George Lucas',
         'planets': [1, 2, 3]}]
    films = film_repository.get_all()
    assert len(films) == 1
    assert films[0].title == 'A New Hope'


def test_find_by_id(film_repository):
    film_repository.collection.find_one.return_value = {'id': 1, 'title': 'A New Hope', 'release_date': '1977-05-25',
                                                        'director': 'George Lucas', 'planets': [1, 2, 3]}
    film = film_repository.find_by_id(1)
    assert film.title == 'A New Hope'


def test_update_film(film_repository):
    film_repository.collection.update_one.return_value = None
    film_repository.update(1, {'title': 'The Empire Strikes Back'})
    film_repository.collection.update_one.assert_called_once()


def test_delete_film(film_repository):
    film_repository.collection.delete_one.return_value = None
    film_repository.delete(1)
    film_repository.collection.delete_one.assert_called_once()
