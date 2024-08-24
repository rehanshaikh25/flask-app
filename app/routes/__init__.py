from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__)
    
    # Load the configuration
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)

    # Register Blueprints
    from .routes.index import index_bp
    from .routes.info import info_bp
    from .routes.members import members_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(info_bp)
    app.register_blueprint(members_bp)

    return app
