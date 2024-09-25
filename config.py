import os
import sys
from socket import socket

BASEDIR = os.path.dirname(os.path.abspath("main.py"))

STATIC_FOLDER = os.path.join(sys._MEIPASS, "static") if getattr(sys, "frozen", False) else "static"
TEMPLATE_FOLDER = os.path.join(sys._MEIPASS, "templates") if getattr(sys, "frozen", False) else "templates"

IMAGE_FOLDER = os.path.join("app", STATIC_FOLDER, "images")

APPDATA = (
    os.path.join(os.getenv("LOCALAPPDATA"), "RF KPI Vivo")
    if getattr(sys, "frozen", False)
    else os.path.join("app", STATIC_FOLDER)
)
FILE_FOLDER = os.path.join(APPDATA, "files")
LOG_FOLDER = os.path.join(APPDATA, "logs")

# Check if log folder exists
if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)

# Check if appdata folder exists
if not os.path.exists(APPDATA):
    os.mkdir(APPDATA)


def clear_folder(folder_path: str):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate over each file and delete it
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        return True
    except Exception as e:
        print(f"Error occurred while clearing folder: {e}")
        return False


# Check if file folder exits
if not os.path.exists(FILE_FOLDER):
    os.mkdir(FILE_FOLDER)
else:
    clear_folder(FILE_FOLDER)


def find_available_port():
    with socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


HOST = "127.0.0.1"
PORT = find_available_port()


class Config:
    FLASK_DEBUG = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "configuration.db")
    SECRET_KEY = b"\xa5\xca'z\xda\xe6\x835C\x11\x8c\xc0\x85\x1e\xeeK\x9c\xf6\xef\xe1`|\xe75"
