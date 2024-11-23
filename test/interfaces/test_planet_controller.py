from unittest.mock import MagicMock

import pytest
from flask import Flask

from app.interfaces.controllers.planet_controller import planet_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(planet_bp, url_prefix='/planets')
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.planet_repository.PlanetRepository.db', mock_db)
    monkeypatch.setattr('app.infrastructure.repositories.planet_repository.PlanetRepository.collection', mock_db)
    return mock_db


def test_add_planet(client):
    response = client.post('/planets/', json={
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'film': 'A New Hope'
    })
    assert response.status_code == 201
    assert 'Planet added successfully' in response.json['message']


def test_get_all_planets(client, mock_db):
    mock_db.find.return_value = [{
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'film': 'A New Hope'
    }]
    response = client.get('/planets/')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_planet_by_id(client, mock_db):
    mock_db.find_one.return_value = {
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'film': 'A New Hope'
    }
    response = client.get('/planets/1')
    assert response.status_code == 200
    assert 'name' in response.json


def test_update_planet(client):
    response = client.put('/planets/1', json={
        'name': 'Hoth',
        'climate': 'frozen',
        'terrain': 'ice plains',
        'film': 'The Empire Strikes Back'
    })
    assert response.status_code == 200
    assert 'Planet updated successfully' in response.json['message']


def test_delete_planet(client):
    response = client.delete('/planets/1')
    assert response.status_code == 200
    assert 'Planet deleted successfully' in response.json['message']
