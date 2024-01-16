from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.database import init_db
from app.config import set_config
from app.route import create_route


def create_app(testing: bool = False):
    app = Flask(__name__)

    csrf = CSRFProtect()
    csrf.init_app(app)

    set_config(app)
    init_db(app)
    create_route(app)

    if testing:
        app.config.update(TESTING=True)

    return app
