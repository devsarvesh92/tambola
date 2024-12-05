from abc import ABC, abstractmethod

from src.domain.claim_result import ClaimResult
from src.domain.ticket import Ticket


class BaseClaimStrategy(ABC):
    """
    Abstract class for claim strategy
    """

    @abstractmethod
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
        raise NotImplementedError

    def is_claim_made_fastest(
        self, *, required_numbers: list[int], announced_numbers: list[int]
    ) -> bool:
        """
        Check if the claim is made fastest

        :param ticket: ticket
        :type ticket: Ticket

        :param announced_numbers: announced numbers
        :type announced_numbers: list[int]

        :return: True if claim is made fastest, False otherwise
        :rtype: bool
        """
        if not announced_numbers:
            return False

        last_number: int = announced_numbers[-1]

        return True if last_number in required_numbers else False
