import datetime

from app.infrastructure.schemas import mongo


class FilmRepository:
    @staticmethod
    def save(film):
        film_data = {
            "title": film.title,
            "release_date": film.release_date,
            "director": film.director,
            "planets": film.planets,
            "created_at": film.created_at,
            "updated_at": film.updated_at
        }
        return mongo.db.films.insert_one(film_data)

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
