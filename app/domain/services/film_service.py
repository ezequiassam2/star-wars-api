from app.domain.models.film import Film
from app.infrastructure.repositories.film_repository import FilmRepository

class FilmService:
    @staticmethod
    def create_film(data):
        film = Film(**data)
        FilmRepository.save(film)
        return film

    @staticmethod
    def get_all_films():
        return FilmRepository.get_all()

    @staticmethod
    def get_film_by_id(film_id):
        return FilmRepository.get_by_id(film_id)

    @staticmethod
    def update_film(film_id, data):
        FilmRepository.update(film_id, data)

    @staticmethod
    def delete_film(film_id):
        FilmRepository.delete(film_id)