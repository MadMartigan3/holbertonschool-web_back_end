#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
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
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

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
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from Base64 decoded value

        Args:
            decoded_base64_authorization_header: the decoded Base64 string

        Returns:
            A tuple (email, password) or (None, None)
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password

        Args:
            user_email: the user's email
            user_pwd: the user's password

        Returns:
            User instance or None
        """
        # Si user_email est None ou pas une string
        if user_email is None or not isinstance(user_email, str):
            return None

        # Si user_pwd est None ou pas une string
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Rechercher les utilisateurs avec cet email
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        # Si aucun utilisateur trouvé
        if not users or len(users) == 0:
            return None

        # Récupérer le premier utilisateur (email devrait être unique)
        user = users[0]

        # Vérifier si le mot de passe est valide
        if not user.is_valid_password(user_pwd):
            return None

        # Retourner l'utilisateur
        return user
