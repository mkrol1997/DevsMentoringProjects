from flask import Flask
from .config import validate_path

app = Flask(__name__)


def create_app():
    app.config['debug'] = True
    validate_path()

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
