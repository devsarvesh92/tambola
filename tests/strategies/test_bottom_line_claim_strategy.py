import pytest
from src.strategies.bottom_line_claim_strategy import BottomLineClaimStrategy

pytestmark = pytest.mark.bottom_line_claim_strategy


def test_bottom_line_valid_completion(ticket):

    bottom_line_claim_strategy = BottomLineClaimStrategy()

    claim_result = bottom_line_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[90, 9, 25, 56, 64, 83],
    )

    assert claim_result.name == "ACCEPTED"


def test_bottom_line_incomplete_numbers(ticket):
    bottom_line_claim_strategy = BottomLineClaimStrategy()

    claim_result = bottom_line_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 0, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"


def test_bottom_line_late_claim(ticket):
    bottom_line_claim_strategy = BottomLineClaimStrategy()

    claim_result = bottom_line_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[90, 9, 25, 56, 64, 83, 12],
    )

    assert claim_result.name == "REJECTED"
