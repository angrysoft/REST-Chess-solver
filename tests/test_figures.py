import pytest
from restchess.domain.model import (
    Bishop, Board, FigureFactory, King, Knight, Pawn, Queen, Rook
)
from restchess.domain.exceptions import FigureNotFound, FiledNotExist


def test_king_list_moves():
    board = Board(True)
    f = King("D1", board)
    available_moves = f.list_available_moves()
    available_moves.sort()
    excpectet_moves = ["C1", "C2", "D2", "E1", "E2"]
    assert available_moves == excpectet_moves


def test_queen_list_moves():
    board = Board(True)
    f = Queen("D1", board)
    available_moves = f.list_available_moves()
    available_moves.sort()
    excpectet_moves = [
        "D8",
        "D7",
        "D6",
        "H5",
        "D5",
        "G4",
        "D4",
        "A4",
        "F3",
        "D3",
        "B3",
        "E2",
        "D2",
        "C2",
        "H1",
        "G1",
        "F1",
        "E1",
        "C1",
        "B1",
        "A1",
    ]
    excpectet_moves.sort()
    assert available_moves == excpectet_moves


def test_rook_list_moves():
    board = Board(True)
    f = Rook("D1", board)
    available_moves = f.list_available_moves()
    available_moves.sort()
    excpectet_moves = [
        "D8",
        "D7",
        "D6",
        "D5",
        "D4",
        "D3",
        "D2",
        "H1",
        "G1",
        "F1",
        "E1",
        "C1",
        "B1",
        "A1",
    ]
    excpectet_moves.sort()
    assert available_moves == excpectet_moves


def test_bishop_list_moves():
    board = Board(True)
    f = Bishop("D1", board)
    available_moves = f.list_available_moves()
    available_moves.sort()
    excpectet_moves = ["H5", "G4", "A4", "F3", "B3", "E2", "C2"]
    excpectet_moves.sort()
    assert available_moves == excpectet_moves


def test_knight_list_moves():
    board = Board(True)
    f = Knight("D1", board)
    available_moves = f.list_available_moves()
    available_moves.sort()
    excpectet_moves = ["E3", "C3", "F2", "B2"]
    excpectet_moves.sort()
    assert available_moves == excpectet_moves


def test_pawn_list_moves():
    board = Board(True)
    f = Pawn("D1", board)
    available_moves = f.list_available_moves()
    available_moves.sort()
    excpectet_moves = ["D2", "D3"]
    excpectet_moves.sort()
    assert available_moves == excpectet_moves


def test_wrong_figure():
    with pytest.raises(FigureNotFound):
        board = Board()
        figure = FigureFactory.create_figure("rooks", "a1", board)
