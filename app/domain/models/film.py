from datetime import datetime
from app.infrastructure.schemas import mongo

class Film:
    def __init__(self, title, release_date, director, planets):
        self.title = title
        self.release_date = release_date
        self.director = director
        self.planets = planets
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        film = {
            "title": self.title,
            "release_date": self.release_date,
            "director": self.director,
            "planets": self.planets,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return mongo.db.films.insert_one(film)

    @staticmethod
    def get_all():
        return mongo.db.films.find()

    @staticmethod
    def get_by_id(film_id):
        return mongo.db.films.find_one({"_id": film_id})

    @staticmethod
    def update(film_id, data):
        data["updated_at"] = datetime.now()
        return mongo.db.films.update_one({"_id": film_id}, {"$set": data})

    @staticmethod
    def delete(film_id):
        return mongo.db.films.delete_one({"_id": film_id})