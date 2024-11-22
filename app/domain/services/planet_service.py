from app.domain.models.planet import Planet


class PlanetService:
    def __init__(self, planet_repository):
        self.repository = planet_repository

    def create_planet(self, data):
        planet = Planet(**data)
        self.repository.save(planet)
        return planet

    def get_all_planets(self):
        return self.repository.get_all()

    def get_planet_by_id(self, planet_id):
        return self.repository.get_by_id(planet_id)

    def update_planet(self, planet_id, data):
        self.repository.update(planet_id, data)

    def delete_planet(self, planet_id):
        self.repository.delete(planet_id)
