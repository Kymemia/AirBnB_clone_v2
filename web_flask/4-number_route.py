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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """property that returns C followed
    by the value of the text variable"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """property that returns Python,
    followed by the value of the text variable"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """property that displays 'n is a number'
    only if n is an integer"""
    if n.isdigit() or (n.startswith('-') and n[1:].isdigit()):
        return f"{n} is a number"


if __name__ == "__main__":
    """ensure the application is running
    on 0.0.0.0, port 5000
    """
    app.run(host="0.0.0.0", port=5000, debug=True)
