from datetime import datetime

class Film:
    def __init__(self, title, release_date, director, planets):
        self.title = title
        self.release_date = release_date
        self.director = director
        self.planets = planets
        self.created_at = datetime.now()
        self.updated_at = datetime.now()