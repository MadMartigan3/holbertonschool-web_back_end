#!/usr/bin/env python3
"""
Module pour le chiffrement de mots de passe
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash un mot de passe avec un salt en utilisant bcrypt

    Args:
        password: Le mot de passe en clair (string)

    Returns:
        Le mot de passe hashé avec salt (bytes)
    """
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Vérifie si un mot de passe correspond à un hash bcrypt

    Args:
        hashed_password: Le mot de passe hashé (bytes)
        password: Le mot de passe en clair à vérifier (string)

    Returns:
        True si le mot de passe correspond, False sinon
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
