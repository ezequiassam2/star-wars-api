from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.domain.services.film_service import FilmService
from app.infrastructure.repositories.film_repository import FilmRepository
from app.infrastructure.schemas.film_schema import FilmSchema
from app.interfaces.validation import ValidationSchema

service = FilmService(FilmRepository())
schema = ValidationSchema(FilmSchema())
film_bp = Blueprint('film_bp', __name__)


@film_bp.route('/', methods=['POST'])
def create_film():
    data = request.get_json()
    try:
        valid_data = schema.validate(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    film = service.create_film(valid_data)
    return jsonify({"message": "Film added successfully", "film": schema.serialize(film)}), 201


@film_bp.route('/', methods=['GET'])
def get_all_films():
    films = service.get_all_films()
    return jsonify(schema.serialize(films, many=True)), 200


@film_bp.route('/<int:film_id>', methods=['GET'])
def get_film_by_id(film_id):
    film = service.get_film_by_id(film_id)
    return jsonify(schema.serialize(film)), 200


@film_bp.route('/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    data = request.get_json()
    try:
        valid_data = schema.validate(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    service.update_film(film_id, valid_data)
    return jsonify({"message": "Film updated successfully"}), 200


@film_bp.route('/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    service.delete_film(film_id)
    return jsonify({"message": "Film deleted successfully"}), 200
