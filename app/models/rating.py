from app import db

class Rating(db.Model):
    
    brand_url = db.Column(db.String)
    brand_name = db.Column(db.String)
    brand_rating = db.Column(db.String)
    brand_summary = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    

    def to_string(self):
        return f"{self.id}: {self.brand_name}, {self.brand_rating}"


