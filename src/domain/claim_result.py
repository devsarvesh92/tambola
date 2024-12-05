"""
Define the ClaimResult enum
"""

from enum import Enum, auto


class ClaimResult(str, Enum):
    """
    Claim result enum
    """

    ACCEPTED = auto()
    REJECTED = auto()

    def __str__(self) -> str:
        return self.name.lower()
