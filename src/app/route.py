from flask import Flask
from app.controllers import formula_controller


def create_route(app: Flask):
    @app.route("/", methods=["GET"])
    def index():
        return "<h1>Flask Latex Sample</h1>"

    @app.route("/latex_to_image", methods=["POST"])
    def latex_to_image():
        return formula_controller.show()
