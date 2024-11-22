from datetime import datetime


class Planet:
    def __init__(self, name, climate, terrain, film, _id=None, created_at=None, updated_at=None):
        self._id = _id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.films = film
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
