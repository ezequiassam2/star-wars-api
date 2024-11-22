from datetime import datetime

from app.infrastructure.repositories.base_repository import BaseRepository
from app.infrastructure.utils import to_object_id


class FilmRepository(BaseRepository):
    def __init__(self):
        super().__init__('films')

    def save(self, film):
        if film.id is None:
            film.id = self.get_next_sequence('film_id')
        return self.collection.insert_one(film.__dict__)

    def get_all(self):
        return self.collection.find()

    def get_by_id(self, film_id):
        return self.collection.find_one({"film_id": to_object_id(film_id)})

    def update(self, film_id, data):
        data["updated_at"] = datetime.now()
        return self.collection.update_one({"film_id": to_object_id(film_id)}, {"$set": data.__dict__})

    def delete(self, film_id):
        return self.collection.delete_one({"film_id": to_object_id(film_id)})
