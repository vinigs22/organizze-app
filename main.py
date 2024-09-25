import os

import webview

from app import create_app
from app.extensions import socketio
from config import HOST, PORT

app = create_app()


def run_socketio(app, host, port):
    socketio.run(app=app, host=host, port=port, allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    window = webview.create_window("RF KPI Vivo", f"http://{HOST}:{PORT}", min_size=(1240, 600), maximized=True)
    webview.start(run_socketio, (app, HOST, PORT), debug=False)

    # Force the running server to stop
    os._exit(0)
