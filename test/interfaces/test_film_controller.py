from datetime import datetime
from unittest.mock import MagicMock

import pytest
from flask import Flask

from app.interfaces.controllers.film_controller import film_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(film_bp, url_prefix='/films')
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.film_repository.FilmRepository.db', mock_db)
    monkeypatch.setattr('app.infrastructure.repositories.film_repository.FilmRepository.collection', mock_db)
    return mock_db


def test_create_film(client, mock_db):
    mock_db.planets.find_one.return_value = True
    mock_db.update_one.return_value = True

    response = client.post('/films/', json={
        'title': 'A New Hope',
        'release_date': '1977-05-25',
        'director': 'George Lucas',
        'planets': [1, 2, 3]
    })
    assert response.status_code == 201
    assert 'Film added successfully' in response.json['message']


def test_create_film_validation_error(client):
    response = client.post('/films/', json={
        'release_date': '1977-05-25',
        'director': 'George Lucas',
        'planets': [1, 2, 3]
    })
    assert response.status_code == 400
    assert 'title' in response.json


def test_create_film_planet_not_found(client, mock_db, monkeypatch):
    mock_db.planets.find_one.return_value = None

    response = client.post('/films/', json={
        'title': 'A New Hope',
        'release_date': '1977-05-25',
        'director': 'George Lucas',
        'planets': [999]
    })
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Planet with id 999 does not exist'


def test_get_all_films(client, mock_db):
    mock_db.find.return_value = [{
        'id': 1,
        'title': 'A New Hope',
        'release_date': datetime.strptime('1977-05-25', "%Y-%m-%d"),
        'director': 'George Lucas',
        'planets': [1, 2, 3]
    }]

    response = client.get('/films/')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_film_by_id(client, mock_db):
    mock_db.find_one.return_value = {
        'id': 1,
        'title': 'A New Hope',
        'release_date': datetime.strptime('1980-05-21', "%Y-%m-%d"),
        'director': 'George Lucas',
        'planets': [1, 2, 3]
    }
    response = client.get('/films/1')
    assert response.status_code == 200
    assert 'title' in response.json


def test_update_film(client):
    response = client.put('/films/1', json={
        'title': 'The Empire Strikes Back',
        'release_date': '1980-05-21',
        'director': 'Irvin Kershner',
        'planets': [1, 2, 3]
    })
    assert response.status_code == 200
    assert 'Film updated successfully' in response.json['message']


def test_delete_film(client):
    response = client.delete('/films/1')
    assert response.status_code == 200
    assert 'Film deleted successfully' in response.json['message']
