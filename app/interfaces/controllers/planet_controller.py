from flask import Blueprint, request, jsonify
from app.domain.services.planet_service import PlanetService

planet_bp = Blueprint('planet_bp', __name__)

@planet_bp.route('/', methods=['POST'])
def add_planet():
    data = request.get_json()
    planet = PlanetService.create_planet(data)
    return jsonify({"message": "Planet added successfully", "planet": planet}), 201

@planet_bp.route('/', methods=['GET'])
def get_planets():
    planets = PlanetService.get_all_planets()
    return jsonify([planet for planet in planets]), 200

@planet_bp.route('/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = PlanetService.get_planet_by_id(planet_id)
    return jsonify(planet), 200

@planet_bp.route('/<planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.get_json()
    PlanetService.update_planet(planet_id, data)
    return jsonify({"message": "Planet updated successfully"}), 200

@planet_bp.route('/<planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    PlanetService.delete_planet(planet_id)
    return jsonify({"message": "Planet deleted successfully"}), 200