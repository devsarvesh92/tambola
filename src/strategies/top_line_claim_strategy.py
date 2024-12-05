"""
Top Line Claim Strategy
"""

from typing import Any
from src.domain.claim_result import ClaimResult
from src.domain.ticket import Ticket
from src.strategies.base_claim_strategy import BaseClaimStrategy


class TopLineClaimStrategy(BaseClaimStrategy):
    """
    Top line claim strategy
    """

    def validate(self, *, ticket: Ticket, numbers_announced: list[int]) -> ClaimResult:
        """
        Validate the claim

        :param ticket: ticket
        :type ticket: Ticket

        :param numbers_announced: numbers announced
        :type numbers_announced: list[int]

        :return: claim result
        :rtype: ClaimResult
        """
        top_row: list[Any] = ticket.rows[0]
        numbers_in_top_row: list[int] = [int(number) for number in top_row if number]

        numbers_in_top_row_set: set[int] = set(numbers_in_top_row)
        numbers_announced_set: set[int] = set(numbers_announced)

        return (
            ClaimResult.ACCEPTED
            if numbers_in_top_row_set.issubset(numbers_announced_set)
            and self.is_claim_made_fastest(
                required_numbers=numbers_in_top_row, announced_numbers=numbers_announced
            )
            else ClaimResult.REJECTED
        )