from datetime import datetime


class Planet:
    def __init__(self, name, climate, terrain, film, id=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        # obs: a relação entre planetas e filmes é de muitos para muitos entretanto seguindo a orientação do desafio foi mantido como um único filme
        self.film = film
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
