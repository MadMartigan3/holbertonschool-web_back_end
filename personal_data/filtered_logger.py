#!/usr/bin/env python3
"""Module for filtering and obfuscating sensitive information in log."""
import re
from typing import List


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
