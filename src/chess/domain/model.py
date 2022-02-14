from __future__ import annotations
from abc import ABC, abstractmethod
from string import ascii_lowercase
from typing import List


class Board:
    pass


class Field:
    def __init__(self, coordinate: str) -> None:
        self._check_coordinate(coordinate)
        self._coordinate = coordinate

    def _check_coordinate(self, coordinate: str):
        letters_allowed: List[str] = [c for c in ascii_lowercase[0:8]]

        errors = False
        if len(coordinate) > 2:
            errors = True

        letter, number = [c for c in coordinate]
        if letter not in letters_allowed or int(number) > 8 or int(number):
            errors = True

        if errors:
            raise ValueError("Field does not exist")


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
