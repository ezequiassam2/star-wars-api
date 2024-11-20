from app.domain.models.planet import Planet

class PlanetService:
    @staticmethod
    def create_planet(data):
        planet = Planet(**data)
        planet.save()
        return planet

    @staticmethod
    def get_all_planets():
        return Planet.get_all()

    @staticmethod
    def get_planet_by_id(planet_id):
        return Planet.get_by_id(planet_id)

    @staticmethod
    def update_planet(planet_id, data):
        Planet.update(planet_id, data)

    @staticmethod
    def delete_planet(planet_id):
        Planet.delete(planet_id)