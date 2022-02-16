from typing import Any, Dict
from flask import Flask, jsonify

from restchess.domain.exceptions import FiledNotExist, FigureNotFound
from restchess.domain.model import Board, FigureFactory

app = Flask(__name__)


@app.route("/api/v1/<figure_name>/<field>")
def available_moves(figure_name: str, field: str):
    result: Dict[str, Any] = {
        "availableMoves": [],
        "error": None,
        "figure": figure_name,
        "currentField": field.upper(),
    }
    status = 200

    try:
        board = Board(empty=True)
        figure = FigureFactory.create_figure(figure_name, field, board)
        result["availableMoves"] = figure.list_available_moves()
    except FigureNotFound:
        result["error"] = "Figure does not exist."
        status = 404
    except FiledNotExist:
        result["error"] = "Field does not exist."
        status = 409

    return jsonify(result), status


@app.route("/api/v1/<figure_name>/<current_field>/<dest_field>")
def valid_move(figure_name: str, current_field: str, dest_field: str):
    result: Dict[str, Any] = {
        "move": "valid",
        "figure": figure_name,
        "error": False,
        "currentField": current_field.upper(),
        "destField": dest_field.upper(),
    }

    status = 200

    try:
        board = Board(empty=True)
        figure = FigureFactory.create_figure(figure_name, current_field, board)
        if not figure.validate_move(dest_field):
            result["move"] = "invalid"
            result["error"] = "Current move is not permitted."
    except FigureNotFound:
        result["error"] = "Figure does not exist."
        result["move"] = "invalid"
        status = 404
    except FiledNotExist:
        result["error"] = "Field does not exist."
        result["move"] = "invalid"
        status = 409

    return jsonify(result), status


if __name__ == "__main__":
    app.run(debug=True)
