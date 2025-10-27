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
        # Si path est None, retourne True
        if path is None:
            return True

        # Si excluded_paths est None ou vide, retourne True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normaliser le path en ajoutant un / à la fin s'il n'y en a pas
        # (pour être "slash tolerant")
        if not path.endswith('/'):
            path = path + '/'

        # Vérifier si le path est dans excluded_paths
        if path in excluded_paths:
            return False

        # Si le path n'est pas dans excluded_paths, retourne True
        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request

        Args:
            request: Flask request object

        Returns:
            None for now (will be implemented later)
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request

        Args:
            request: Flask request object

        Returns:
            None for now (will be implemented later)
        """
        return None
