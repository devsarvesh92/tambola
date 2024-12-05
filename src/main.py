"""
Main entry point for Tambola Claim Validator demonstration

NOTE: This file serves as a reference implementation/blueprint only.
For actual usage, please refer to the test suite which provides comprehensive
coverage of all features and edge cases.

Key Components Demonstrated:
- Ticket creation
- Claim validation
- Strategy selection
- Basic usage patterns

"""

from src.domain.claim_result import ClaimResult
from src.domain.ticket import Ticket
from src.domain.claim_type import ClaimType
from src.factory.claim_strategy_factory import ClaimStrategyFactory
from src.strategies.base_claim_strategy import BaseClaimStrategy


def validate_claim(
    ticket_data: list[str], numbers_announced: list[int], claim_type: ClaimType
) -> bool:
    """
    Validate a claim in the Tambola game

    Example usage:
    >>> ticket_data = [
    ...     "4,16,_,_,48,_,63,76,_",
    ...     "7,_,23,38,_,52,_,_,80",
    ...     "9,_,25,_,_,56,64,_,83"
    ... ]
    >>> numbers = [90, 4, 46, 63, 89, 16, 76, 48]
    >>> validate_claim(ticket_data, numbers, ClaimType.TOP_ROW)
    True
    """
    ticket: Ticket = Ticket(raw_ticket=ticket_data)
    strategy: BaseClaimStrategy = ClaimStrategyFactory.create(claim_type)
    result: ClaimResult = strategy.validate(
        ticket=ticket, numbers_announced=numbers_announced
    )
    return result


def main():
    # Example from problem statement
    ticket_data = [
        "4,16,_,_,48,_,63,76,_",
        "7,_,23,38,_,52,_,_,80",
        "9,_,25,_,_,56,64,_,83",
    ]

    # Demonstrate different claim scenarios
    print("\nTambola Claim Validator Demo")
    print("-" * 30)

    # Top Row Example
    numbers = [90, 4, 46, 63, 89, 16, 76, 48]
    result = validate_claim(ticket_data, numbers, ClaimType.TOP_LINE)
    print(f"Numbers announced: {numbers}")
    print(f"Claim Result: {result.name}")

    # Late Claim Example
    numbers = [90, 4, 46, 63, 89, 16, 76, 48, 12]
    result = validate_claim(ticket_data, numbers, ClaimType.TOP_LINE)
    print(f"Numbers announced: {numbers}")
    print(f"Claim Result: {result.name}")

    # Early Five Example
    numbers = [4, 16, 48, 63, 76]
    result = validate_claim(ticket_data, numbers, ClaimType.EARLY_FIVE)
    print(f"Numbers announced: {numbers}")
    print(f"Claim Result: {result.name}")


if __name__ == "__main__":
    main()
