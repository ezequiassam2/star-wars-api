from app.interfaces.controllers.planet_controller import planet_bp
from app.interfaces.controllers.film_controller import film_bp

def register_routes(app):
    app.register_blueprint(planet_bp, url_prefix='/planets')
    app.register_blueprint(film_bp, url_prefix='/films')