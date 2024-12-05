import pytest

from src.domain.claim_result import ClaimResult


pytestmark = pytest.mark.claim_type


def test_all_claim_types_present():

    assert len(ClaimResult) == 2
    assert ClaimResult.ACCEPTED.name == "ACCEPTED"
    assert ClaimResult.REJECTED.name == "REJECTED"
