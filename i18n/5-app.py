#!/usr/bin/env python3
"""
Flask app: mock login + translated messages.

- Mock users via ?login_as=<id>
- Store current user in flask.g.user (or None)
- Force locale via ?locale=fr|en, else use Accept-Language

Functions:
    gettext: Get translated text for message IDs based on current locale
    _: Shorthand alias for gettext function for convenient translation
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from typing import Any, Dict, Optional


_.__doc__ = """
Translate a message ID to the current locale.

This function is an alias for gettext that provides internationalization
support by translating message IDs to localized strings based on the
current user's locale.

Args:
    message_id (str): The message identifier to translate

Returns:
    str: The translated message for the current locale
"""


class Config:
    """Set Babel's default locale ("en") and timezone ("UTC")."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale() -> str:
    """Determine the best match with our supported languages."""
    forced = request.args.get("locale", type=str)
    if forced in app.config["LANGUAGES"]:
        return forced
    return (request.accept_languages.best_match(app.config["LANGUAGES"]) or
            app.config["BABEL_DEFAULT_LOCALE"])


babel.init_app(app, locale_selector=get_locale)


def get_user() -> Optional[Dict[str, Any]]:
    """
    Get the current user based on login_as parameter.

    Returns:
        dict: User dictionary if found, None otherwise
    """
    uid = request.args.get("login_as", type=int)
    if uid and uid in users:
        return users[uid]
    return None


@app.before_request
def before_request():
    """
    Run before each request.

    Attaches the current user (if any) to flask.g and sets up
    the locale for template access.
    """
    g.user = get_user()
    g.locale = get_locale()


@app.route("/")
def index() -> Any:
    """
    Route handler for the home page with user authentication display.

    This function handles GET requests to the root URL ('/') and renders
    the main index template with internationalization support and user
    authentication status display.

    Returns:
        str: The rendered HTML content from the '5-index.html' template
             with appropriate translations and user information
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
