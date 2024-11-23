from unittest.mock import MagicMock

import pytest

from app.infrastructure.repositories.base_repository import BaseRepository


@pytest.fixture
def mock_db(monkeypatch):
    mock_db = MagicMock()
    monkeypatch.setattr('app.infrastructure.repositories.base_repository.mongo', MagicMock(db=mock_db))
    return mock_db


@pytest.fixture
def base_repository():
    return BaseRepository('test_collection')


def test_collection_property(base_repository, mock_db):
    assert base_repository.collection
    mock_db.assert_not_called()


def test_get_next_sequence(base_repository, mock_db):
    mock_db.counters.find_one_and_update.return_value = {'sequence_value': 1}
    sequence_value = base_repository.get_next_sequence('test_sequence')
    assert sequence_value == 1
    mock_db.counters.find_one_and_update.assert_called_once_with(
        {'_id': 'test_sequence'},
        {'$inc': {'sequence_value': 1}},
        return_document=True,
        upsert=True
    )
