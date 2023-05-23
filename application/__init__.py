from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env=None):
    app = Flask(__name__)

    if env == "TEST":
        pass
    else:
        app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////application/database/movies.db'
        app.config["DEBUG"] = True
        Bootstrap(app)

    from application.database import database_service
    db.init_app(app)
    app.app_context().push()
    database_service.init_app(db)

    CORS(app)

    from application.controllers import api
    api.init_app(app)

    return app
