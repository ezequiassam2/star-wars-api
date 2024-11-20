from datetime import datetime

class Planet:
    def __init__(self, name, climate, terrain, films):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.films = films
        self.created_at = datetime.now()
        self.updated_at = datetime.now()