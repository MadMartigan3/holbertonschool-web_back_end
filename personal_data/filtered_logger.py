#!/usr/bin/env python3
"""Module for filtering and obfuscating sensitive information in log."""
import re
from typing import List
import logging


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
