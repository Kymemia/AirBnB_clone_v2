#!/usr/bin/python3
"""This is a script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """property that returns statement on success"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """property that returns statement on success"""
    return "HBNB"


if __name__ == "__main__":
    """ensure the application is running
    on 0.0.0.0, port 5000
    """
    app.run(host="0.0.0.0", port=5000, debug=True)
