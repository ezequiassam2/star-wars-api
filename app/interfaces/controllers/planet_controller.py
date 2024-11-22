from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.domain.services.planet_service import PlanetService
from app.infrastructure.repositories.planet_repository import PlanetRepository
from app.infrastructure.schemas.planet_schema import PlanetSchema
from app.interfaces.validation import ValidationSchema

service = PlanetService(PlanetRepository())
schema = ValidationSchema(PlanetSchema())
planet_bp = Blueprint('planet_bp', __name__)


@planet_bp.route('/', methods=['POST'])
def add_planet():
    data = request.get_json()
    try:
        valid_data = schema.validate(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    planet = service.create_planet(valid_data)
    return jsonify({"message": "Planet added successfully", "planet": schema.serialize(planet)}), 201


@planet_bp.route('/', methods=['GET'])
def get_planets():
    planets = service.get_all_planets()
    return jsonify(schema.serialize(planets, many=True)), 200


@planet_bp.route('/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = service.get_planet_by_id(planet_id)
    return jsonify(schema.serialize(planet)), 200


@planet_bp.route('/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.get_json()
    try:
        valid_data = schema.validate(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    service.update_planet(planet_id, valid_data)
    return jsonify({"message": "Planet updated successfully"}), 200


@planet_bp.route('/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    service.delete_planet(planet_id)
    return jsonify({"message": "Planet deleted successfully"}), 200
