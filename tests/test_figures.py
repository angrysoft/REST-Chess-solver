import imp
from zoneinfo import available_timezones


from chess.domain.model import King, Field

def test_king_list_moves():
    f = King(Field("D1"))
    available_moves = f.list_available_moves()
    