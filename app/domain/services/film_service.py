from app.domain.models.film import Film


class FilmService:
    def __init__(self, film_repository):
        self.repository = film_repository

    def create_film(self, data):
        film = Film(**data)
        self.repository.save(film)
        return film

    def get_all_films(self):
        return self.repository.get_all()

    def get_film_by_id(self, film_id):
        return self.repository.get_by_id(film_id)

    def update_film(self, film_id, data):
        self.repository.update(film_id, data)

    def delete_film(self, film_id):
        self.repository.delete(film_id)
