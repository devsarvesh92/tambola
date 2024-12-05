import pytest
from src.strategies.full_house_claim_strategy import FullHouseClaimStrategy
from src.domain.ticket import Ticket

pytestmark = pytest.mark.full_house_claim_strategy


def test_full_house_valid_completion():

    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    full_house_claim_strategy = FullHouseClaimStrategy()

    claim_result = full_house_claim_strategy.validate(
        ticket=ticket,
        numbers_announced=[4, 16, 48, 63, 76, 7, 23, 38, 52, 80, 9, 25, 56, 64, 83],
    )

    assert claim_result.name == "ACCEPTED"


def test_full_house_incomplete_numbers():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
    full_house_claim_strategy = FullHouseClaimStrategy()

    claim_result = full_house_claim_strategy.validate(
        ticket=ticket, numbers_announced=[90, 0, 46, 63, 89, 16, 76, 48, 12]
    )

    assert claim_result.name == "REJECTED"


def test_full_house_late_claim():
    ticket = Ticket(
        raw_ticket=[
            "4,16,_,_,48,_,63,76,_",
            "7,_,23,38,_,52,_,_,80",
            "9,_,25,_,_,56,64,_,83",
        ]
    )
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
