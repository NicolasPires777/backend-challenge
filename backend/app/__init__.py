from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import configure_routes
    configure_routes(app)

    # Swagger UI configuration
    SWAGGER_URL = '/api/docs'  # URL to access Swagger UI
    API_URL = '/static/OpenAPI.yaml'  # Path to your OpenAPI.yaml file
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Test application"
        }
    )
    
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
