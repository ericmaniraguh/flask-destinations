from flask import Blueprint, jsonify, request
from database import db
from models import Destination

main_bp = Blueprint('main', __name__)

# Create Routes
@main_bp.route('/')
def home():
    return 'Hello World'

# GET all destinations
# http://localhost:5000/destinations    
@main_bp.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([d.to_dict() for d in destinations]), 200


# GET a single destination by ID
# http://localhost:5000/destinations/<id>
@main_bp.route('/destinations/<int:id>', methods=['GET'])
def get_destination(id):
    destination = Destination.query.get_or_404(id)
    return jsonify(destination.to_dict()), 200


# POST create new destination
# http://localhost:5000/destinations

@main_bp.route('/destinations', methods=['POST'])
def create_destination():
    data = request.get_json() or {}
    required_fields = ['destination', 'country', 'rating', 'image']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    new_destination = Destination(
        destination=data['destination'],
        country=data['country'],
        rating=data['rating'],
        image=data['image']
    )
    
    db.session.add(new_destination)
    db.session.commit()
    return jsonify(new_destination.to_dict()), 201


# POST create multiple destinations (Batch)
# http://localhost:5000/destinations/batch
@main_bp.route('/destinations/batch', methods=['POST'])
def create_many_destinations():
    data = request.get_json() or []
    
    if not isinstance(data, list):
        return jsonify({"message": "Input must be a list of destinations"}), 400

    required_fields = ['destination', 'country', 'rating', 'image']
    new_destinations = []

    try:
        for item in data:
            if not all(field in item for field in required_fields):
                return jsonify({"message": f"Missing required fields in item: {item}"}), 400
            
            new_dest = Destination(
                destination=item['destination'],
                country=item['country'],
                rating=item['rating'],
                image=item['image']
            )
            db.session.add(new_dest)
            new_destinations.append(new_dest)
        
        db.session.commit()
        return jsonify([d.to_dict() for d in new_destinations]), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# PUT update destination by ID
# http://localhost:5000/destinations/<id>
@main_bp.route('/destinations/<int:id>', methods=['PUT'])
def update_destination(id):
    destination = Destination.query.get_or_404(id)
    data = request.get_json() or {}

    # Update only provided fields
    if 'destination' in data:
        destination.destination = data['destination']
    if 'country' in data:
        destination.country = data['country']
    if 'rating' in data:
        destination.rating = data['rating']
    if 'image' in data:
        destination.image = data['image']

    db.session.commit()
    return jsonify(destination.to_dict()), 200


# DELETE a destination by ID
# http://localhost:5000/destinations/<id>
@main_bp.route('/destinations/<int:id>', methods=['DELETE'])
def delete_destination(id):
    destination = Destination.query.get_or_404(id)
    db.session.delete(destination)
    db.session.commit()
    return jsonify({"message": "Destination deleted successfully!"}), 200
