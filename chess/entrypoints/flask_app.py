from typing import Any, Dict
from flask import Flask, jsonify

from chess.domain.exceptions import FiledNotExist, FigureNotFound
from chess.domain.model import FigureFactory

app = Flask(__name__)


@app.route("/api/v1/<figure_name>/<field>")
def available_moves(figure_name: str, field: str):
    result: Dict[str, Any] = {
        "availableMoves": [],
        "error": None,
        "figure": figure_name,
        "currentField": field,
    }
    status = 200

    try:
        figure = FigureFactory.create_figure(figure_name, field)
        result["availableMoves"] = figure.list_available_moves()
    except FigureNotFound:
        result["error"] = "Figure does not exist."
        status = 404
    except FiledNotExist:
        result["error"] = "Field does not exist."
        status = 409

    return jsonify(result), status


if __name__ == "__main__":
    app.run(debug=True)
