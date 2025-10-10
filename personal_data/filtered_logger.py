#!/usr/bin/env python3
"""Module for filtering and obfuscating sensitive information in log."""
import re
from typing import List, Tuple
import logging


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates sensitive field values in a log message using regex.

    Args:
        fields: List of field names to obfuscate
        redaction: String to replace sensitive field values with
        message: The log message string to process
        separator: Character that separates fields in the message

    Returns:
        The log message with specified fields obfuscated
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}",
                  message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for filtering information in logs."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with fields to redact.

        Args:
            fields: List of field names to obfuscate in log messages
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record and filter sensitive field values.

        Args:
            record: LogRecord instance to format

        Returns:
            Formatted log message with sensitive fields redacted
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data with PII redaction.

    Returns:
        A configured Logger object named 'user_data' with RedactingFormatter
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger
