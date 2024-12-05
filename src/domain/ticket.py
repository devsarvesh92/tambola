"""
Represents the ticket class
"""

from typing import Any
from src.exceptions import InvalidTicketError


class Ticket:
    """
    Ticket domain class
    """

    EXPECTED_ROWS = 3
    EXPECTED_COLUMNS = 9

    def __init__(self, raw_ticket: list[str]):
        """
        Initialize the ticket

        :param raw_ticket: raw ticket string
        :raise InvalidTicketError: if the ticket is invalid
        """

        if not self._is_ticket_valid(raw_ticket=raw_ticket):
            raise InvalidTicketError("Invalid ticket")

        self.rows: list[list[Any]] = self._parse_ticket(raw_ticket=raw_ticket)

    def _is_ticket_valid(self, *, raw_ticket: list[str]) -> bool:
        """
        Validate the ticket

        :param raw_ticket: raw ticket string
        :type raw_ticket: str

        :return: True if valid, False otherwise
        :rtype: bool
        """

        if len(raw_ticket) != self.EXPECTED_ROWS:
            return False

        for ticket in raw_ticket:
            if len(ticket.split(",")) != self.EXPECTED_COLUMNS:
                return False

            # Check if all charaters are digits or _
            if not all(char.isdigit() or char == "_" for char in ticket.split(",")):
                return False

        return True

    def _parse_ticket(self, *, raw_ticket: str) -> list[list[Any]]:
        """
        Parse the ticket

        :param raw_ticket: raw ticket string
        :type raw_ticket: str

        :return: parsed ticket
        :rtype: list[list[Any]]
        """
        rows = []

        for ticket in raw_ticket:
            row = ticket.split(",")
            rows.append([int(char) if char != "_" else None for char in row])
        return rows
