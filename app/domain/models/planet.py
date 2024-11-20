from datetime import datetime
from app.infrastructure.schemas import mongo

class Planet:
    def __init__(self, name, climate, diameter, population, films):
        self.name = name
        self.climate = climate
        self.diameter = diameter
        self.population = population
        self.films = films
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        planet = {
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "population": self.population,
            "films": self.films,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return mongo.db.planets.insert_one(planet)

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