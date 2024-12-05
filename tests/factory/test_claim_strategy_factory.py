import pytest
from src.domain.claim_type import ClaimType
from src.strategies.base_claim_strategy import BaseClaimStrategy
from src.strategies.top_line_claim_strategy import TopLineClaimStrategy
from src.strategies.middle_line_claim_strategy import MiddleLineClaimStrategy
from src.strategies.bottom_line_claim_strategy import BottomLineClaimStrategy
from src.strategies.early_five_claim_strategy import EarlyFiveClaimStrategy
from src.strategies.full_house_claim_strategy import FullHouseClaimStrategy
from src.factory.claim_strategy_factory import ClaimStrategyFactory

pytestmark = pytest.mark.claim_strategy_factory


def test_creates_top_line_strategy():
    strategy = ClaimStrategyFactory.create(ClaimType.TOP_LINE)
    assert isinstance(strategy, TopLineClaimStrategy)


def test_creates_middle_line_strategy():
    strategy = ClaimStrategyFactory.create(ClaimType.MIDDLE_LINE)
    assert isinstance(strategy, MiddleLineClaimStrategy)


def test_creates_bottom_line_strategy():
    strategy = ClaimStrategyFactory.create(ClaimType.BOTTOM_LINE)
    assert isinstance(strategy, BottomLineClaimStrategy)


def test_creates_early_five_strategy():
    strategy = ClaimStrategyFactory.create(ClaimType.EARLY_FIVE)
    assert isinstance(strategy, EarlyFiveClaimStrategy)


def test_creates_full_house_strategy():
    strategy = ClaimStrategyFactory.create(ClaimType.FULL_HOUSE)
    assert isinstance(strategy, FullHouseClaimStrategy)


def test_all_strategies_follow_base_interface():
    for claim_type in ClaimType:
        strategy = ClaimStrategyFactory.create(claim_type)
        assert isinstance(strategy, BaseClaimStrategy)


def test_raises_error_for_invalid_claim_type():
    with pytest.raises(ValueError):
        ClaimStrategyFactory.create("INVALID_TYPE")
