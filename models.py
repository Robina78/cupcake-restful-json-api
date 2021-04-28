"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
default_image = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """ ocnnect to database"""

    db.app = app
    db.init_app(app)



class Cupcake(db.Model):

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, default=default_image)


    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }


    def __repr__(self):
        return f"< Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image} >"     
