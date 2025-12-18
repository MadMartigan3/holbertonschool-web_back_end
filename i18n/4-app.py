#!/usr/bin/env python3
"""
Flask app: force locale via URL parameter with Flask-Babel.

- Supports locales: en, fr
- If a request has ?locale=fr|en, use it; otherwise use Accept-Language.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """set Babel’s default locale ("en") and timezone ("UTC")"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Determine the best match with our supported languages"""
    forced = request.args.get("locale", type=str)
    if forced and forced in app.config["LANGUAGES"]:
        return forced
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """This function handles GET requests to the root URL ('/')
    and renders the main index template for the application."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
