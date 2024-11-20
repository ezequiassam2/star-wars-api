from app.domain.models.planet import Planet

class PlanetRepository:
    @staticmethod
    def save(planet):
        return planet.save()

    @staticmethod
    def get_all():
        return Planet.get_all()

    @staticmethod
    def get_by_id(planet_id):
        return Planet.get_by_id(planet_id)

    @staticmethod
    def update(planet_id, data):
        return Planet.update(planet_id, data)

    @staticmethod
    def delete(planet_id):
        return Planet.delete(planet_id)