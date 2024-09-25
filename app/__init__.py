from flask import Flask

from app.extensions import socketio
from config import STATIC_FOLDER, TEMPLATE_FOLDER, Config


def create_app(config_class=Config):
    # Start the app
    app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
    app.config.from_object(config_class)

    # Initialize SocketIO
    socketio.init_app(app, async_mode="threading")

    # Register blueprints here

    return app
