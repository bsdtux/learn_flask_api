import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")

db = SQLAlchemy()

from models.models import Course


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATA_DIR}/courses.db"

    @app.route("/")
    def index():
        return {"ping": "pong"}

    from .api_routes import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    db.init_app(app)

    return app
