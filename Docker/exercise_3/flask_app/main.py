from flask import Blueprint, request
from .config import SAVE_TO_FILE

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
def main():
    with open(SAVE_TO_FILE, "a") as file:
        [file.writelines(f"{parameter}={request.args[parameter]}\n") for parameter in request.args]

    return "<h1>Send URL parameters to save in parameters.txt</h1>"
