import pytest
from src.strategies.full_house_claim_strategy import FullHouseClaimStrategy

pytestmark = pytest.mark.full_house_claim_strategy


def test_full_house_valid_completion(ticket):

    full_house_claim_strategy = FullHouseClaimStrategy()

    claim_result = full_house_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[4, 16, 48, 63, 76, 7, 23, 38, 52, 80, 9, 25, 56, 64, 83],
    )

    assert claim_result.name == "ACCEPTED"


def test_full_house_incomplete_numbers(ticket):
    full_house_claim_strategy = FullHouseClaimStrategy()

    claim_result = full_house_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 0, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"


def test_full_house_late_claim(ticket):
    full_house_claim_strategy = FullHouseClaimStrategy()

    claim_result = full_house_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[
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
            100,
        ],
    )

    assert claim_result.name == "REJECTED"
