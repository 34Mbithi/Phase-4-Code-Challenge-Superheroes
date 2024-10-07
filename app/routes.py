from flask import Blueprint, jsonify, request, abort
from app.models import Hero, Power, HeroPower, db

hero_routes = Blueprint('hero_routes', __name__)

# GET /heroes
@hero_routes.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# GET /heroes/:id
@hero_routes.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [{
            "hero_id": hp.hero_id,
            "id": hp.id,
            "power": {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            },
            "power_id": hp.power_id,
            "strength": hp.strength
        } for hp in hero.hero_powers]
    })

# GET /powers
@hero_routes.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# GET /powers/:id
@hero_routes.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.to_dict())

# PATCH /powers/:id
@hero_routes.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power not found"}), 404

    data = request.json
    description = data.get('description')

    if not description or len(description) < 20:
        return jsonify({"errors": ["Description must be at least 20 characters long"]}), 400

    power.description = description
    db.session.commit()

    return jsonify(power.to_dict())

# POST /hero_powers
@hero_routes.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if strength not in ['Strong', 'Average', 'Weak']:
        return jsonify({"errors": ["Invalid strength value"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 404

    new_hero_power = HeroPower(
        hero_id=hero_id,
        power_id=power_id,
        strength=strength
    )
    
    db.session.add(new_hero_power)
    db.session.commit()

    return jsonify({
        "id": new_hero_power.id,
        "hero_id": hero.id,
        "power_id": power.id,
        "strength": strength,
        "hero": hero.to_dict(),
        "power": power.to_dict()
    }), 201