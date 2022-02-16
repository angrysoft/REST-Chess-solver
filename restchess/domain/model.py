from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List
import chess

from restchess.domain.exceptions import FigureNotFound, FieldNotExist


class Board:
    def __init__(self, empty: bool = False) -> None:
        _fen: str | None = chess.STARTING_FEN
        if empty:
            _fen = None
        self._board = chess.Board(_fen)

    def get_available_moves(self, figure: BaseFigure):
        """Return List of available moves from filed"""
        self._board.set_piece_at(
            chess.SQUARE_NAMES.index(figure.current_field),
            chess.Piece(figure.figure_type(), chess.WHITE),
        )

        moves = [
            chess.SQUARE_NAMES[move.to_square].upper()
            for move in self._board.legal_moves
        ]
        return moves

    def is_valid_move(self, figure: BaseFigure, dest_field: str):
        """Check if figure can move from current file to dest filed"""
        self._board.set_piece_at(
            chess.SQUARE_NAMES.index(figure.current_field),
            chess.Piece(figure.figure_type(), chess.WHITE),
        )
        move = chess.Move.from_uci(f"{figure.current_field}{dest_field}".lower())
        return move in self._board.legal_moves


class Figure(ABC):
    def __init__(self, field: str) -> None:
        if field.lower() not in chess.SQUARE_NAMES:
            raise FieldNotExist
        self.current_field = field.lower()

    @abstractmethod
    def list_available_moves(self) -> List[str]:
        pass

    @abstractmethod
    def validate_move(self, dest_field: str) -> bool:
        pass


class BaseFigure(Figure):
    def __init__(self, field: str, board: Board) -> None:
        super().__init__(field)
        self._board = board

    def list_available_moves(self) -> List[str]:
        return self._board.get_available_moves(self)

    def validate_move(self, dest_field: str) -> bool:
        return self._board.is_valid_move(self, dest_field)

    @staticmethod
    def figure_type() -> int:
        return -1


class King(BaseFigure):
    @staticmethod
    def figure_type() -> int:
        return chess.KING


class Queen(BaseFigure):
    @staticmethod
    def figure_type() -> int:
        return chess.QUEEN


class Rook(BaseFigure):
    @staticmethod
    def figure_type() -> int:
        return chess.ROOK


class Bishop(BaseFigure):
    @staticmethod
    def figure_type() -> int:
        return chess.BISHOP


class Knight(BaseFigure):
    @staticmethod
    def figure_type() -> int:
        return chess.KNIGHT


class Pawn(BaseFigure):
    @staticmethod
    def figure_type() -> int:
        return chess.PAWN


class FigureFactory:
    @staticmethod
    def create_figure(figure_name: str, field: str, board: Board) -> Figure:
        figures: Dict[str, Any] = {
            "king": King,
            "queen": Queen,
            "rook": Rook,
            "bishop": Bishop,
            "knight": Knight,
            "pawn": Pawn,
        }

        if figure_name not in figures:
            raise FigureNotFound

        return figures[figure_name](field, board)
