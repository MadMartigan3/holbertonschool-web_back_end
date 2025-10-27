#!/usr/bin/env python3
""" function called filter_datum that returns the log message obfuscated """

import mysql.connector
import logging
import os
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Implement the format method to filter values
            in incoming log records using filter_datum.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
        Function called filter_datum that returns the log message obfuscated
        Args:
            fields: List of strings representing all fields to obfuscate
            redaction: String representing by what the field will be obfuscated
            message: String representing the log line
            separator: Character is separating all fields
        Returns:
            Log message obfuscated.
    """
    pattern = (r'(' + '|'.join(fields) + r')=([^' +
               re.escape(separator) + r']*)')
    return re.sub(pattern, r'\1=' + redaction, message)


def get_logger() -> logging.Logger:
    """
        Create and return a logger named 'user_data'
        with specific configuration.
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    formatter: RedactingFormatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Create and return a connector to the database using environment variables.
    """
    username: str = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password: str = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host: str = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database: str = os.getenv('PERSONAL_DATA_DB_NAME')

    connection: mysql.connector.connection.MySQLConnection = (
        mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
    )

    return connection


def main() -> None:
    """
    Main function that retrieves all users from database and logs them
    with filtered PII data.
    """

    logger = get_logger()
    db = get_db()

    try:
        cursor = db.cursor()
        query = ("SELECT name, email, phone, ssn, password, ip, "
                 "last_login, user_agent FROM users;")
        cursor.execute(query)

        for row in cursor:
            log_message = (
                f"name={row[0]}; email={row[1]}; phone={row[2]}; "
                f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
                f"last_login={row[6]}; user_agent={row[7]};"
            )

            logger.info(log_message)

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
