from app.domain.models.planet import Planet
from app.infrastructure.repositories.planet_repository import PlanetRepository

class PlanetService:
    @staticmethod
    def create_planet(data):
        planet = Planet(**data)
        PlanetRepository.save(planet)
        return planet

    @staticmethod
    def get_all_planets():
        return PlanetRepository.get_all()

    @staticmethod
    def get_planet_by_id(planet_id):
        return PlanetRepository.get_by_id(planet_id)

    @staticmethod
    def update_planet(planet_id, data):
        PlanetRepository.update(planet_id, data)

    @staticmethod
    def delete_planet(planet_id):
        PlanetRepository.delete(planet_id)