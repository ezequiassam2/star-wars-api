from flask import Flask

from app.infrastructure import initialize_db
from app.interfaces.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    initialize_db(app)
    register_routes(app)
    return app
