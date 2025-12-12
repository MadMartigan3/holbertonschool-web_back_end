#!/usr/bin/env python3
"""Auth file"""
import uuid
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import Base, User


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    bpwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(bpwd, salt)
    return hashed_pwd


def _generate_uuid() -> str:
    """Generate a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {existing_user.email} already exists")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email=email,
                                         hashed_password=hashed_pwd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Verify if password is hash"""
        try:
            existing_user = self._db.find_user_by(email=email)
            bpwd = password.encode('utf-8')
            if bcrypt.checkpw(bpwd, existing_user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Find the user corresponding to the email, generate a new UUID
        and store it in the database as the user’s session_id"""
        try:
            existing_user = self._db.find_user_by(email=email)
            new_uuid = _generate_uuid()
            self._db.update_user(existing_user.id, session_id=new_uuid)
            return new_uuid
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find the user with a session_id"""
        if session_id is None:
            return None
        try:
            existing_user = self._db.find_user_by(session_id=session_id)
            return existing_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Find the user with a session_id"""
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Update the reset_token"""
        try:
            existing_user = self._db.find_user_by(email=email)
            new_uuid = _generate_uuid()
            self._db.update_user(existing_user.id, reset_token=new_uuid)
            return new_uuid
        except NoResultFound:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the password"""
        try:
            existing_user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password)
            self._db.update_user(existing_user.id,
                                 hashed_password=hashed_pwd, reset_token=None)
        except NoResultFound:
            raise ValueError
        return None