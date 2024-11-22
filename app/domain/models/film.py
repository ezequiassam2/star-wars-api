from datetime import datetime


class Film:
    def __init__(self, title, release_date, director, planets, film_id=None, created_at=None, updated_at=None):
        self.id = film_id
        self.title = title
        self.release_date = release_date
        self.director = director
        self.planets = planets
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()