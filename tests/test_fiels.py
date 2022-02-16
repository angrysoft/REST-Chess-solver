import pytest
from chess.domain.exceptions import FiledNotExist
from chess.domain.model import Field


def test_filed_no():
    f = Field("A1")
    assert f.no == 0
    f = Field("B1")
    assert f.no == 1
    f = Field("A2")
    assert f.no == 8
    f = Field("A3")
    assert f.no == 16
    f = Field("A4")
    assert f.no == 24


def test_filed_out_of_board():
    with pytest.raises(FiledNotExist):
        Field("A15")
    with pytest.raises(FiledNotExist):
        Field("z1")
    with pytest.raises(FiledNotExist):
        Field("y1")


def test_field_eq():
    f1 = Field("A1")
    f2 = Field("A1")
    assert f1 == f2


def test_field_neq():
    f1 = Field("A1")
    f2 = Field("A3")
    assert f1 != f2


def test_filed_in_list():
    filed_list = [
        Field("A1"),
        Field("A2"),
        Field("B1"),
        Field("C1"),
        Field("D7")
    ]
    f = Field("B1")
    assert f in filed_list


def test_filed_not_in_list():
    filed_list = [
        Field("A1"),
        Field("A2"),
        Field("B1"),
        Field("C1"),
        Field("D7")
    ]
    f = Field("E1")
    assert f not in filed_list


def test_filed_from_number():
    f = Field.field_from_number(0)
    assert str(f) == "A1"
    f1 = Field.field_from_number(8)
    assert str(f1) == "A2"
