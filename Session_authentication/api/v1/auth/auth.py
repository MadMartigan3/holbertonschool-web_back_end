#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path

        Args:
            path: the path to check
            excluded_paths: list of paths that don't require authentication

        Returns:
            True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path = path + '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request

        Args:
            request: Flask request object

        Returns:
            The value of Authorization header or None
        """
        # Si request est None, retourne None
        if request is None:
            return None

        # Si request ne contient pas la clé Authorization, retourne None
        if 'Authorization' not in request.headers:
            return None

        # Sinon, retourne la valeur du header Authorization
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request

        Args:
            request: Flask request object

        Returns:
            None for now (will be implemented later)
        """
        return None
