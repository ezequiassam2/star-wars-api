from datetime import datetime

from app.infrastructure import get_db


class PlanetRepository:
    def __init__(self):
        self.mongo = get_db()
    # todo verificar se o planeta já existe
    def save(self, planet):
        planet_data = {
            "name": planet.name,
            "climate": planet.climate,
            "terrain": planet.terrain,
            "films": planet.films,
            "created_at": planet.created_at,
            "updated_at": planet.updated_at
        }
        return self.mongo.db.planets.insert_one(planet_data)

    def get_all(self):
        return self.mongo.db.planets.find()

    def get_by_id(self, planet_id):
        return self.mongo.db.planets.find_one({"_id": planet_id})

    def update(self, planet_id, data):
        data["updated_at"] = datetime.now()
        return self.mongo.db.planets.update_one({"_id": planet_id}, {"$set": data})

    def delete(self, planet_id):
        return self.mongo.db.planets.delete_one({"_id": planet_id})
