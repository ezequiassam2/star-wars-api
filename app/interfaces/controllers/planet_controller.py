from flask import Blueprint, request, jsonify
from app.domain.services.planet_service import PlanetService
from app.infrastructure.schemas.planet_schema import PlanetSchema

planet_bp = Blueprint('planet_bp', __name__)

@planet_bp.route('/', methods=['POST'])
def add_planet():
    data = request.get_json()
    schema = PlanetSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    planet = PlanetService.create_planet(data)
    return jsonify({"message": "Planet added successfully", "planet": schema.dump(planet)}), 201

@planet_bp.route('/', methods=['GET'])
def get_planets():
    planets = PlanetService.get_all_planets()
    schema = PlanetSchema(many=True)
    return jsonify(schema.dump(planets)), 200

@planet_bp.route('/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = PlanetService.get_planet_by_id(planet_id)
    schema = PlanetSchema()
    return jsonify(schema.dump(planet)), 200

@planet_bp.route('/<planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.get_json()
    schema = PlanetSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    PlanetService.update_planet(planet_id, data)
    return jsonify({"message": "Planet updated successfully"}), 200

@planet_bp.route('/<planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    PlanetService.delete_planet(planet_id)
    return jsonify({"message": "Planet deleted successfully"}), 200