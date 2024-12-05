import pytest
from src.strategies.top_line_claim_strategy import TopLineClaimStrategy

pytestmark = pytest.mark.top_line_claim_strategy


def test_top_line_valid_completion(ticket):

    top_line_claim_strategy = TopLineClaimStrategy()

    claim_result = top_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 4, 46, 63, 89, 16, 76, 48]
    )

    assert claim_result.name == "ACCEPTED"


def test_top_line_incomplete_numbers(ticket):
    top_line_claim_strategy = TopLineClaimStrategy()

    claim_result = top_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 0, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"


def test_top_line_late_claim(ticket):

    top_line_claim_strategy = TopLineClaimStrategy()

    claim_result = top_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 4, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"
