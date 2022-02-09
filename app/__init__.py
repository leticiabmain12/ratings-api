from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app,db)
    from app.models.rating import Rating

    # # Add endpoint
    #register blueprints here
    from .routes import ratings_bp
    app.register_blueprint(ratings_bp)
    

    return app