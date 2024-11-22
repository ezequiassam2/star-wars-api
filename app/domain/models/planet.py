from datetime import datetime


class Planet:
    def __init__(self, name, climate, terrain, film, id=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        #obs: A relação entre planetas e filmes é de muitos para muitos entretanto foi feito dessa forma para serguir o escopo do que foi estabalecido no documento
        self.film = film
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'film': self.film,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
