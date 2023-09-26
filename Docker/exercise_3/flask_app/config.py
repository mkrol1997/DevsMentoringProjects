import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(BASE_DIR, 'static')
SAVE_TO_FILE = os.path.join(STATIC_PATH, 'parameters.txt')


def validate_path():
    if not os.path.exists(STATIC_PATH):
        os.mkdir(STATIC_PATH)
