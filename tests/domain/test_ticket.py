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
    assert len(ticket.rows[0]) == ticket.EXPECTED_COLUMNS


def test_raises_invalid_ticket_error():
    invalid_ticket_data = [
        "4,16,_,_,48,_,63,76,_",
        "7,_,23,38,_,52,_,_,80",
        "9,_,25,_,_,56,64,_,83",
        "9,_,25,_,_,56,64,_,83",
    ]
    with pytest.raises(InvalidTicketError):
        Ticket(raw_ticket=invalid_ticket_data)
