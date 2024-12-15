from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    is_in_stock = db.Column(db.Boolean, default=True)

    # Optionally add more fields here, if needed.
    # For example, description, category, etc.

    # You can add the to_dict method directly in your model as an example:
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': self.price,
            'is_in_stock': self.is_in_stock
        }

