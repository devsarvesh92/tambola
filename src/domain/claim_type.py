"""
Claim type module
"""

from enum import Enum, auto


class ClaimType(str, Enum):
    """
    Claim type enum
    """

    TOP_LINE = auto()
    MIDDLE_LINE = auto()
    BOTTOM_LINE = auto()
    FULL_HOUSE = auto()
    EARLY_FIVE = auto()

    def __str__(self) -> str:
        return self.name.lower().replace("_", " ")
