from flask import Flask # type: ignore

def create_app():
    app = Flask(__name__)

    from .routes import configure_routes
    configure_routes(app)

    return app
