#!/usr/bin/env python3
"""
Flask app: locale + timezone selection with Flask-Babel.

Priority rules:
- Locale: URL (?locale) > user setting > Accept-Language > default
- Timezone: URL (?timezone) > user setting > default ("UTC")
"""
from typing import Any, Dict, Optional, List
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """set Babel’s default locale ("en") and timezone ("UTC")"""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel()


def get_user() -> Optional[Dict[str, Optional[str]]]:
    """Get the user"""
    uid = request.args.get("login_as", type=int)
    return users.get(uid) if uid in users else None


@app.before_request
def before_request() -> None:
    """Attach current user to flask.g for this request."""
    g.user = get_user()


def get_locale() -> str:
    """Determine the best match with our supported languages"""
    forced = request.args.get("locale", type=str)
    if forced in app.config["LANGUAGES"]:
        return forced

    user = getattr(g, "user", None)
    if user:
        uloc = user.get("locale")
        if uloc in app.config["LANGUAGES"]:
            return str(uloc)

    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    if match:
        return match

    return app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone() -> str:
    """get timezone"""
    tz = request.args.get("timezone", type=str)
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass

    user = getattr(g, "user", None)
    if user:
        utz = user.get("timezone")
        if isinstance(utz, str):
            try:
                pytz.timezone(utz)
                return utz
            except UnknownTimeZoneError:
                pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


@app.route("/", strict_slashes=False)
def index() -> Any:
    """This function handles GET requests to the root URL ('/')
    and renders the main index template for the application."""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
