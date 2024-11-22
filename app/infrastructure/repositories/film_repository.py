from datetime import datetime

from app.domain.exceptions import PlanetNotFoundException
from app.domain.models.film import Film
from app.infrastructure.repositories.base_repository import BaseRepository


class FilmRepository(BaseRepository):
    def __init__(self):
        super().__init__('films')

    def save(self, film: Film):
        for planet_id in film.planets:
            if not self.db.planets.find_one({'id': planet_id}):
                raise PlanetNotFoundException(planet_id)

        if film.id is None:
            film.id = self.get_next_sequence('film_id')
        return self.collection.update_one({'id': film.id}, {'$set': film.to_dict()}, upsert=True)

    def get_all(self):
        films = self.collection.find({}, {'_id': False})
        if films:
            return [Film(**film) for film in films]
        return None

    def find_by_id(self, film_id: int):
        film_data = self.collection.find_one({'id': film_id}, {'_id': False})
        if film_data:
            return Film(**film_data)
        return None

    def update(self, film_id: int, data: dict):
        data['updated_at'] = datetime.now()
        return self.collection.update_one({'id': film_id}, {'$set': data})

    def delete(self, film_id: int):
        return self.collection.delete_one({'id': film_id})
