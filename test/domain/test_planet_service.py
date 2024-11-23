from unittest.mock import MagicMock

import pytest

from app.domain.services.planet_service import PlanetService
from app.infrastructure.repositories.planet_repository import PlanetRepository


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.planet_repository.PlanetRepository.db', mock_db)
    monkeypatch.setattr('app.infrastructure.repositories.planet_repository.PlanetRepository.collection', mock_db)
    return mock_db


@pytest.fixture
def planet_service():
    repository = PlanetRepository()
    return PlanetService(repository)


def test_create_planet(planet_service, mock_db):
    mock_db.counters.find_one_and_update.return_value = {'sequence_value': 1}

    data = {'name': 'Tatooine', 'climate': 'arid', 'terrain': 'desert', 'film': 'A New Hope'}
    planet = planet_service.create_planet(data)
    assert planet is not None
    assert planet.id == 1
    mock_db.update_one.assert_called_once()


def test_get_all_planets(planet_service, mock_db):
    data = {'name': 'Tatooine', 'climate': 'arid', 'terrain': 'desert', 'film': 'A New Hope'}
    mock_db.find.return_value = [data]
    planets = planet_service.get_all_planets()
    assert len(planets) == 1


def test_get_planet_by_id(planet_service, mock_db):
    data = {'id': 1, 'name': 'Tatooine', 'climate': 'arid', 'terrain': 'desert', 'film': 'A New Hope'}
    mock_db.find_one.return_value = data
    planet = planet_service.get_planet_by_id(1)
    assert planet.name == 'Tatooine'
    mock_db.find_one.assert_called_once_with({'id': 1}, {'_id': False})


def test_update_planet(planet_service, mock_db):
    mock_db.find_one.return_value = {'name': 'Tatooine', 'climate': 'arid', 'terrain': 'desert', 'film': 'A New Hope'}
    update_data = {'name': 'Hoth'}
    planet_service.update_planet(1, update_data)
    mock_db.update_one.assert_called_once_with({'id': 1}, {'$set': update_data})


def test_delete_planet(planet_service, mock_db):
    planet_service.delete_planet(1)
    mock_db.delete_one.assert_called_once_with({'id': 1})
