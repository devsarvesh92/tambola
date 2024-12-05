"""
Full house claim Strategy
"""

from src.domain.claim_result import ClaimResult
from src.domain.ticket import Ticket
from src.strategies.base_claim_strategy import BaseClaimStrategy


class FullHouseClaimStrategy(BaseClaimStrategy):
    """
    Full house claim strategy
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
        all_numbers: list[int] = ticket.get_all_numbers()

        all_numbers_set: set[int] = set(all_numbers)
        numbers_announced_set: set[int] = set(numbers_announced)

        return (
            ClaimResult.ACCEPTED
            if all_numbers_set.issubset(numbers_announced_set)
            and self.is_claim_made_fastest(
                required_numbers=all_numbers,
                announced_numbers=numbers_announced,
            )
            else ClaimResult.REJECTED
        )
