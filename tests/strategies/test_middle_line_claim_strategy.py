import pytest
from src.strategies.middle_line_claim_strategy import MiddleLineClaimStrategy
from src.domain.ticket import Ticket

pytestmark = pytest.mark.middle_line_claim_strategy


def test_middle_line_valid_completion():

    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    middle_line_claim_strategy = MiddleLineClaimStrategy()

    claim_result = middle_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 4, 16, 7, 23, 38, 52, 80]
    )

    assert claim_result.name == "ACCEPTED"


def test_middle_line_incomplete_numbers():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    middle_line_claim_strategy = MiddleLineClaimStrategy()

    claim_result = middle_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 0, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"


def test_middle_line_late_claim():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    middle_line_claim_strategy = MiddleLineClaimStrategy()

    claim_result = middle_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 4, 16, 7, 23, 38, 52, 80, 12]
    )

    assert claim_result.name == "REJECTED"
