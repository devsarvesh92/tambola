"""
Middle Line Claim Strategy
"""

from typing import Any
from src.domain.claim_result import ClaimResult
from src.domain.ticket import Ticket
from src.strategies.base_claim_strategy import BaseClaimStrategy


class MiddleLineClaimStrategy(BaseClaimStrategy):
    """
    Middle line claim strategy
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
        middle_row: list[Any] = ticket.rows[1]
        numbers_in_middle_row: list[int] = [
            int(number) for number in middle_row if number
        ]

        numbers_in_top_row_set: set[int] = set(numbers_in_middle_row)
        numbers_announced_set: set[int] = set(numbers_announced)

        return (
            ClaimResult.ACCEPTED
            if numbers_in_top_row_set.issubset(numbers_announced_set)
            and self.is_claim_made_fastest(
                required_numbers=numbers_in_middle_row,
                announced_numbers=numbers_announced,
            )
            else ClaimResult.REJECTED
        )
