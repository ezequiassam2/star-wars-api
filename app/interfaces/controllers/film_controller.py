from flask import Blueprint, request, jsonify
from app.domain.services.film_service import FilmService
from app.infrastructure.schemas.film_schema import FilmSchema

film_bp = Blueprint('film_bp', __name__)

@film_bp.route('/', methods=['POST'])
def add_film():
    data = request.get_json()
    schema = FilmSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    film = FilmService.create_film(data)
    return jsonify({"message": "Film added successfully", "film": schema.dump(film)}), 201

@film_bp.route('/', methods=['GET'])
def get_films():
    films = FilmService.get_all_films()
    schema = FilmSchema(many=True)
    return jsonify(schema.dump(films)), 200

@film_bp.route('/<film_id>', methods=['GET'])
def get_film(film_id):
    film = FilmService.get_film_by_id(film_id)
    schema = FilmSchema()
    return jsonify(schema.dump(film)), 200

@film_bp.route('/<film_id>', methods=['PUT'])
def update_film(film_id):
    data = request.get_json()
    schema = FilmSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    FilmService.update_film(film_id, data)
    return jsonify({"message": "Film updated successfully"}), 200

@film_bp.route('/<film_id>', methods=['DELETE'])
def delete_film(film_id):
    FilmService.delete_film(film_id)
    return jsonify({"message": "Film deleted successfully"}), 200