from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize the db and API
api = Api(app)
db.init_app(app)

# Create resource for handling plant actions
class PlantByID(Resource):

    def get(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if plant:
            return make_response(jsonify(plant.to_dict()), 200)
        return make_response(jsonify({"message": "Plant not found"}), 404)

    def patch(self, id):
        plant = Plant.query.filter_by(id=id).first()

        if not plant:
            return make_response(jsonify({"message": "Plant not found"}), 404)

        data = request.get_json()

        if 'is_in_stock' in data:
            plant.is_in_stock = data['is_in_stock']

        db.session.commit()

        return make_response(jsonify(plant.to_dict()), 200)

    def delete(self, id):
        plant = Plant.query.filter_by(id=id).first()

        if not plant:
            return make_response(jsonify({"message": "Plant not found"}), 404)

        db.session.delete(plant)
        db.session.commit()

        return make_response('', 204)  # No content

# Add PlantByID resource to the API
api.add_resource(PlantByID, '/plants/<int:id>')

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
