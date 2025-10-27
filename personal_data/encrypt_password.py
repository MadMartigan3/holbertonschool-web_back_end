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
    # Convertir le password string en bytes
    password_bytes = password.encode('utf-8')
    
    # Générer un salt et hasher le mot de passe
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
    return hashed