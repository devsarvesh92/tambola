import pytest

from src.domain.ticket import Ticket


@pytest.fixture
def ticket():
    return Ticket(
        [
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
