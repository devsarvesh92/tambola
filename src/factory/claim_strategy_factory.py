"""Factory for creating claim validation strategies"""

from src.domain.claim_type import ClaimType
from src.strategies.base_claim_strategy import BaseClaimStrategy
from src.strategies.top_line_claim_strategy import TopLineClaimStrategy
from src.strategies.middle_line_claim_strategy import MiddleLineClaimStrategy
from src.strategies.bottom_line_claim_strategy import BottomLineClaimStrategy
from src.strategies.early_five_claim_strategy import EarlyFiveClaimStrategy
from src.strategies.full_house_claim_strategy import FullHouseClaimStrategy


class ClaimStrategyFactory:
    """Factory to create appropriate claim validation strategy"""

    _strategies = {
        ClaimType.TOP_LINE: TopLineClaimStrategy(),
        ClaimType.MIDDLE_LINE: MiddleLineClaimStrategy(),
        ClaimType.BOTTOM_LINE: BottomLineClaimStrategy(),
        ClaimType.EARLY_FIVE: EarlyFiveClaimStrategy(),
        ClaimType.FULL_HOUSE: FullHouseClaimStrategy(),
    }

    @staticmethod
    def create(claim_type: ClaimType) -> BaseClaimStrategy:
        """
        Create appropriate strategy based on claim type

        Args:
            claim_type: Type of claim being made

        Returns:
            Strategy to validate the claim

        Raises:
            ValueError: If claim type is not supported
        """
        strategy = ClaimStrategyFactory._strategies.get(claim_type)
        if not strategy:
            raise ValueError(f"Unsupported claim type: {claim_type}")
        return strategy
