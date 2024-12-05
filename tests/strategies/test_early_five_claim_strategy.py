import pytest
from src.strategies.early_five_claim_strategy import EarlyFiveClaimStrategy

pytestmark = pytest.mark.early_five_claim_strategy


def test_early_five_valid_completion(ticket):

    early_five_claim_strategy = EarlyFiveClaimStrategy()

    claim_result = early_five_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[4, 16, 48, 90, 91, 63, 76],
    )

    assert claim_result.name == "ACCEPTED"


def test_early_five_incomplete_numbers(ticket):
    early_five_claim_strategy = EarlyFiveClaimStrategy()

    claim_result = early_five_claim_strategy.validate(
        ticket=ticket, numbers_announced=[4, 16, 48, 63, 12, 90]
    )

    assert claim_result.name == "REJECTED"


def test_early_five_late_claim(ticket):
    early_five_claim_strategy = EarlyFiveClaimStrategy()

    claim_result = early_five_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[4, 16, 48, 63, 76, 90],
    )

    assert claim_result.name == "REJECTED"
