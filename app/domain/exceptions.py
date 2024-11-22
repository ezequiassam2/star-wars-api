class PlanetNotFoundException(Exception):
    def __init__(self, planet_id):
        self.planet_id = planet_id
        self.message = f"Planet with id {planet_id} does not exist"
        super().__init__(self.message)
