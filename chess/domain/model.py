from __future__ import annotations
from abc import ABC, abstractmethod
from string import ascii_lowercase
from typing import Any, Dict, List

from chess.domain.exceptions import FigureNotFound, FiledNotExist


class Field:
    def __init__(self, coordinate: str) -> None:
        self._field_no = -1
        self._coordinate = coordinate
        self._check_coordinate()

    def _check_coordinate(self):
        letters_allowed: List[str] = [c for c in ascii_lowercase[0:8]]

        if len(self._coordinate) > 2:
            raise FiledNotExist("Field does not exist")

        letter, number = [c for c in self._coordinate]
        no = int(number)

        if letter.lower() not in letters_allowed or no > 8 or no < 1:
            raise FiledNotExist("Field does not exist")

        no -= 1
        self._field_no = letters_allowed.index(letter.lower()) + no + 7 * no

    @property
    def no(self):
        return self._field_no

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Field) and self._field_no == __o._field_no
    
    def __str__(self) -> str:
        return f"{self._coordinate.upper()}"

    @staticmethod
    def field_from_number(num: int):
        board = Board()
        return Field(board.get_field_coordinate_by_number(num))


class Board:
    def __init__(self) -> None:
        self._state: List[Field] = []
        self.create_board()

    def create_board(self):
        self._state.clear()
        for letter in ascii_lowercase[0:8]:
            for number in range(1, 9):
                self._state.append(Field(f"{letter.upper()}{number}"))

    def get_field_coordinate_by_number(self, number: int) -> str:
        return str(self._state[number])


class Figure(ABC):
    def __init__(self, field: Field) -> None:
        self.current_figure_field = field

    @abstractmethod
    def list_available_moves(self) -> List[Field]:
        pass

    @abstractmethod
    def validate_move(self, dest_field: Field) -> bool:
        pass


class King(Figure):
    def list_available_moves(self) -> List[Field]:
        return []

    def validate_move(self, dest_field: Field) -> bool:
        return False


class Queen(Figure):
    def list_available_moves(self) -> List[Field]:
        return []

    def validate_move(self, dest_field: Field) -> bool:
        return False


class Rook(Figure):
    def list_available_moves(self) -> List[Field]:
        return []

    def validate_move(self, dest_field: Field) -> bool:
        return False


class Bishop(Figure):
    def list_available_moves(self) -> List[Field]:
        return []

    def validate_move(self, dest_field: Field) -> bool:
        return False


class Knight(Figure):
    def list_available_moves(self) -> List[Field]:
        return []

    def validate_move(self, dest_field: Field) -> bool:
        return False


class Pawn(Figure):
    def list_available_moves(self) -> List[Field]:
        return []

    def validate_move(self, dest_field: Field) -> bool:
        return False


class FigureFactory:
    @staticmethod
    def create_figure(figure_name: str, field: str) -> Figure:
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

        return figures.get(figure_name)(Field(field))
