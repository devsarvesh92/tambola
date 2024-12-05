import pytest

from src.domain.ticket import Ticket
from src.exceptions import InvalidTicketError


pytestmark = pytest.mark.ticket


def test_valid_ticket_creation():
    valid_ticket_data = [
        "4,16,_,_,48,_,63,76,_",
        "7,_,23,38,_,52,_,_,80",
        "9,_,25,_,_,56,64,_,83",
    ]
    ticket = Ticket(raw_ticket=valid_ticket_data)
    assert len(ticket.rows) == ticket.EXPECTED_ROWS
    assert len(ticket.rows[0]) == 5


def test_raises_invalid_ticket_error():
    invalid_ticket_data = [
        "4,16,_,_,48,_,63,76,_",
        "7,_,23,38,_,52,_,_,80",
        "9,_,25,_,_,56,64,_,83",
        "9,_,25,_,_,56,64,_,83",
    ]
    with pytest.raises(InvalidTicketError):
        Ticket(raw_ticket=invalid_ticket_data)


def test_ticket_should_parse_top_row_correctly():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    assert ticket.get_top_row() == [4, 16, 48, 63, 76]


def test_ticket_should_parse_middle_row_correctly():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    assert ticket.get_middle_row() == [7, 23, 38, 52, 80]


def test_ticket_should_parse_bottom_row_correctly():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    assert ticket.get_bottom_row() == [9, 25, 56, 64, 83]


def test_ticket_should_parse_all_numbers_correctly():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    assert ticket.get_all_numbers() == [
        4,
        16,
        48,
        63,
        76,
        7,
        23,
        38,
        52,
        80,
        9,
        25,
        56,
        64,
        83,
    ]
