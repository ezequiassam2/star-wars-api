from unittest.mock import MagicMock

import pytest

from app.domain.models.planet import Planet
from app.infrastructure.repositories.planet_repository import PlanetRepository


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.planet_repository.PlanetRepository.db', mock_db)
    monkeypatch.setattr('app.infrastructure.repositories.planet_repository.PlanetRepository.collection', mock_db)
    return mock_db


@pytest.fixture
def planet_repository():
    return PlanetRepository()


def test_save_planet(planet_repository):
    planet = Planet(id=None, name='Tatooine', climate='arid', terrain='desert', film='A New Hope')
    planet_repository.get_next_sequence = MagicMock(return_value=1)
    planet_repository.save(planet)
    planet_repository.collection.update_one.assert_called_once()


def test_get_all_planets(planet_repository):
    planet_repository.collection.find.return_value = [
        {'id': 1, 'name': 'Tatooine', 'climate': 'arid', 'terrain': 'desert', 'film': 'A New Hope'}]
    planets = planet_repository.get_all()
    assert len(planets) == 1
    assert planets[0].name == 'Tatooine'


def test_find_by_id(planet_repository):
    planet_repository.collection.find_one.return_value = {'id': 1, 'name': 'Tatooine', 'climate': 'arid',
                                                          'terrain': 'desert', 'film': 'A New Hope'}
    planet = planet_repository.find_by_id(1)
    assert planet.name == 'Tatooine'


def test_update_planet(planet_repository):
    planet_repository.collection.update_one.return_value = None
    planet_repository.update(1, {'name': 'Hoth'})
    planet_repository.collection.update_one.assert_called_once()


def test_delete_planet(planet_repository):
    planet_repository.collection.delete_one.return_value = None
    planet_repository.delete(1)
    planet_repository.collection.delete_one.assert_called_once()
