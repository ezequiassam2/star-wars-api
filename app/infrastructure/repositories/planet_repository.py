from datetime import datetime

from app.domain.models.planet import Planet
from app.infrastructure.repositories.base_repository import BaseRepository


class PlanetRepository(BaseRepository):
    def __init__(self):
        super().__init__('planets')

    def save(self, planet: Planet):
        if planet.id is None:
            planet.id = self.get_next_sequence('planet_id')
        self.collection.update_one({'id': planet.id}, {'$set': planet.to_dict()}, upsert=True)

    def get_all(self):
        planets = self.collection.find({}, {'_id': False})
        if planets:
            return [Planet(**planet) for planet in planets]
        return None

    def find_by_id(self, planet_id: int):
        planet_data = self.collection.find_one({'id': planet_id}, {'_id': False})
        if planet_data:
            return Planet(**planet_data)
        return None

    def update(self, planet_id: int, data: dict):
        data['updated_at'] = datetime.now()
        return self.collection.update_one({'id': planet_id}, {'$set': data})

    def delete(self, planet_id: int):
        return self.collection.delete_one({'id': planet_id})
