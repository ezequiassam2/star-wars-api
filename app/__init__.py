from flask import Flask
from app.infrastructure.schemas import initialize_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    initialize_db(app)
    return app