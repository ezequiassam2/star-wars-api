from datetime import datetime

from app.infrastructure import get_db
from app.infrastructure.utils import to_object_id


class FilmRepository:
    def __init__(self):
        self.mongo = get_db()

    def save(self, film):
        film_data = {
            "title": film.title,
            "release_date": film.release_date,
            "director": film.director,
            "planets": film.planets,
            "created_at": film.created_at,
            "updated_at": film.updated_at
        }
        return self.mongo.db.films.insert_one(film_data)

    def get_all(self):
        return self.mongo.db.films.find()

    def get_by_id(self, film_id):
        return self.mongo.db.films.find_one({"_id": to_object_id(film_id)})

    def update(self, film_id, data):
        data["updated_at"] = datetime.now()
        return self.mongo.db.films.update_one({"_id": to_object_id(film_id)}, {"$set": data})

    def delete(self, film_id):
        return self.mongo.db.films.delete_one({"_id": to_object_id(film_id)})
