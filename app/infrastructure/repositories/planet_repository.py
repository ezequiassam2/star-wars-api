from datetime import datetime
from app.infrastructure.schemas import mongo

class PlanetRepository:
    @staticmethod
    def save(planet):
        planet_data = {
            "name": planet.name,
            "climate": planet.climate,
            "terrain": planet.terrain,
            "films": planet.films,
            "created_at": planet.created_at,
            "updated_at": planet.updated_at
        }
        return mongo.db.planets.insert_one(planet_data)

    @staticmethod
    def get_all():
        return mongo.db.planets.find()

    @staticmethod
    def get_by_id(planet_id):
        return mongo.db.planets.find_one({"_id": planet_id})

    @staticmethod
    def update(planet_id, data):
        data["updated_at"] = datetime.now()
        return mongo.db.planets.update_one({"_id": planet_id}, {"$set": data})

    @staticmethod
    def delete(planet_id):
        return mongo.db.planets.delete_one({"_id": planet_id})