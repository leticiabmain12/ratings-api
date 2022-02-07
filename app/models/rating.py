from app import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String)
    brand_rating = db.Column(db.String)

    def to_string(self):
        return f"{self.id}: {self.brand_name}, {self.brand_rating}"


