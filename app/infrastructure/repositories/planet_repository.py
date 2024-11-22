from datetime import datetime

from app.infrastructure.repositories.base_repository import BaseRepository


class PlanetRepository(BaseRepository):
    def __init__(self):
        super().__init__('planets')

    # todo verificar se o planeta já existe
    def save(self, planet):
        if planet.id is None:
            planet.id = self.get_next_sequence('planet_id')
        self.collection.insert_one(planet.__dict__)

    def get_all(self):
        return self.collection.find()

    def get_by_id(self, planet_id):
        return self.collection.find_one({"id": planet_id})

    def update(self, planet_id, data):
        data["updated_at"] = datetime.now()
        return self.collection.update_one({"id": planet_id}, {"$set": data.__dict__})

    def delete(self, planet_id):
        return self.collection.delete_one({"id": planet_id})
