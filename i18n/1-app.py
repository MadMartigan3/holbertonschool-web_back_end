#!/usr/bin/env python3
"""Basic Flask app using babel in 1-app.py"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """set Babel’s default locale ("en") and timezone ("UTC")"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """This function handles GET requests to the root URL ('/')
    and renders the main index template for the application."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
