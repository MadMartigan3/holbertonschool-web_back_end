#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string

        Args:
            base64_authorization_header: the Base64 string to decode

        Returns:
            The decoded value as UTF8 string or None
        """
        # Si base64_authorization_header est None, retourne None
        if base64_authorization_header is None:
            return None

        # Si base64_authorization_header n'est pas une string, retourne None
        if not isinstance(base64_authorization_header, str):
            return None

        # Essayer de décoder le Base64
        try:
            # Décoder le Base64
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convertir les bytes en string UTF-8
            return decoded_bytes.decode('utf-8')
        except Exception:
            # Si ce n'est pas un Base64 valide, retourne None
            return None
