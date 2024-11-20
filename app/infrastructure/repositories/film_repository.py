from app.domain.models.film import Film

class FilmRepository:
    @staticmethod
    def save(film):
        return film.save()

    @staticmethod
    def get_all():
        return Film.get_all()

    @staticmethod
    def get_by_id(film_id):
        return Film.get_by_id(film_id)

    @staticmethod
    def update(film_id, data):
        return Film.update(film_id, data)

    @staticmethod
    def delete(film_id):
        return Film.delete(film_id)