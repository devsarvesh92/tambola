import pytest


pytestmark = pytest.mark.claim_type


def test_all_claim_types_present():
    from src.domain.claim_type import ClaimType

    assert len(ClaimType) == 5
    assert ClaimType.TOP_LINE.name == "TOP_LINE"
    assert ClaimType.MIDDLE_LINE.name == "MIDDLE_LINE"
    assert ClaimType.BOTTOM_LINE.name == "BOTTOM_LINE"
    assert ClaimType.FULL_HOUSE.name == "FULL_HOUSE"
    assert ClaimType.EARLY_FIVE.name == "EARLY_FIVE"
