#!/usr/bin/env python3
""" Authentication module for API """
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Template for authentication system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns True if the path is not in the list of strings excluded_paths:
        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths
        You can assume excluded_paths contains string path always ending by a /
        This method must be slash tolerant:
        path=/api/v1/status and path=/api/v1/status/
        must be returned False if excluded_paths contains /api/v1/status/
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        If request is None, returns None
        If request doesn't contain the header key Authorization, returns None
        Otherwise, return the value of the header request Authorization
        """
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None

        return request.headers.get("Authorization")

    User = TypeVar("User")

    def current_user(self, request=None) -> User:
        """
        returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME", "_my_session_id")

        return request.cookies.get(session_name)
    