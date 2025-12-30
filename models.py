from database import db

class Destination(db.Model):
    id = db.Column(db.Integer, db.Sequence('destination_id_seq'), primary_key=True)
    destination = db.Column(db.String(100))
    country = db.Column(db.String(100)) 
    rating = db.Column(db.Float)
    image = db.Column(db.String(200))

    # Convert to dictionary which facilitate the conversion to JSON
    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'country': self.country,
            'rating': self.rating,
            'image': self.image
        }



