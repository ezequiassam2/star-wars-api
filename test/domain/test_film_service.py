from unittest.mock import MagicMock

import pytest

from app.domain.services.film_service import FilmService
from app.infrastructure.repositories.film_repository import FilmRepository


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.film_repository.FilmRepository.db', mock_db)
    monkeypatch.setattr('app.infrastructure.repositories.film_repository.FilmRepository.collection', mock_db)
    return mock_db


@pytest.fixture
def film_service():
    repository = FilmRepository()
    return FilmService(repository)


def test_create_film(film_service, mock_db):
    mock_db.planets.find_one.return_value = True
    mock_db.counters.find_one_and_update.return_value = {'sequence_value': 1}

    data = {'title': 'A New Hope', 'release_date': '1977-05-25', 'director': 'George Lucas', 'planets': [1]}
    film = film_service.create_film(data)
    assert film is not None
    assert film.id == 1


def test_get_film_by_id(film_service, mock_db):
    mock_db.find_one.return_value = {'title': 'A New Hope', 'release_date': '1977-05-25', 'director': 'George Lucas'}
    film = film_service.get_film_by_id(1)
    assert film.title == 'A New Hope'
    mock_db.find_one.assert_called_once_with({'id': 1}, {'_id': False})


def test_get_all_films(film_service, mock_db):
    mock_db.find.return_value = [
        {'id': 1, 'title': 'A New Hope', 'release_date': '1977-05-25', 'director': 'George Lucas'}]
    films = film_service.get_all_films()
    assert isinstance(films, list)
    assert len(films) == 1
    mock_db.find.assert_called_once()


def test_update_film(film_service, mock_db):
    mock_db.find_one.return_value = {'id': 1, 'title': 'A New Hope', 'release_date': '1977-05-25',
                                     'director': 'George Lucas'}
    update_data = {'title': 'The Empire Strikes Back'}
    film_service.update_film(1, update_data)
    mock_db.update_one.assert_called_once_with({'id': 1}, {'$set': update_data})


def test_delete_film(film_service, mock_db):
    film_service.delete_film(1)
    mock_db.delete_one.assert_called_once_with({'id': 1})
