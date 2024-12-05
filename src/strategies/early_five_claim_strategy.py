"""
Early five claim Strategy
"""

from src.domain.claim_result import ClaimResult
from src.domain.ticket import Ticket
from src.strategies.base_claim_strategy import BaseClaimStrategy


class EarlyFiveClaimStrategy(BaseClaimStrategy):
    """
    Early five claim strategy
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

        if len(numbers_announced) < 5:
            return ClaimResult.REJECTED

        all_numbers: list[int] = ticket.get_all_numbers()
        all_numbers_set: set[int] = set(all_numbers)
        numbers_announced_set: set[int] = set(numbers_announced)
        matched_numbers: set[int] = all_numbers_set.intersection(numbers_announced_set)

        if len(matched_numbers) != 5:
            return ClaimResult.REJECTED

        matched_list = [
            number for number in numbers_announced if number in matched_numbers
        ]

        return (
            ClaimResult.ACCEPTED
            if self.is_claim_made_fastest(
                required_numbers=matched_list[:5],
                announced_numbers=numbers_announced,
            )
            else ClaimResult.REJECTED
        )
