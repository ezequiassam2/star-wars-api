from app.domain.models.film import Film

class FilmService:
    @staticmethod
    def create_film(data):
        film = Film(**data)
        film.save()
        return film

    @staticmethod
    def get_all_films():
        return Film.get_all()

    @staticmethod
    def get_film_by_id(film_id):
        return Film.get_by_id(film_id)

    @staticmethod
    def update_film(film_id, data):
        Film.update(film_id, data)

    @staticmethod
    def delete_film(film_id):
        Film.delete(film_id)