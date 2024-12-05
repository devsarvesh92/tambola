import pytest
from src.strategies.top_line_claim_strategy import TopLineClaimStrategy
from src.domain.ticket import Ticket

pytestmark = pytest.mark.top_line_claim_strategy


def test_top_line_valid_completion():

    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    top_line_claim_strategy = TopLineClaimStrategy()

    claim_result = top_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 4, 46, 63, 89, 16, 76, 48]
    )

    assert claim_result.name == "ACCEPTED"


def test_top_line_incomplete_numbers():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    top_line_claim_strategy = TopLineClaimStrategy()

    claim_result = top_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 0, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"


def test_top_line_late_claim():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    top_line_claim_strategy = TopLineClaimStrategy()

    claim_result = top_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 4, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"
