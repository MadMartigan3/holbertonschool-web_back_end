#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for Basic Authentication

        Args:
            authorization_header: the Authorization header string

        Returns:
            The Base64 part after 'Basic ' or None
        """
        # Si authorization_header est None, retourne None
        if authorization_header is None:
            return None

        # Si authorization_header n'est pas une string, retourne None
        if not isinstance(authorization_header, str):
            return None

        # Si authorization_header ne commence pas par 'Basic '
        if not authorization_header.startswith('Basic '):
            return None

        # Retourne la valeur après 'Basic ' (après l'espace)
        return authorization_header[6:]
