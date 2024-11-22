from datetime import datetime


class Film:
    def __init__(self, title, release_date, director, id=None, planets=None, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.director = director
        self.planets = planets or []
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'director': self.director,
            'planets': [str(planet_id) for planet_id in self.planets],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
