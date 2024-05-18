#!/usr/bin/python3
"""This module starts a Flask web application.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ defines the page to display at '/'
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')