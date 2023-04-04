#!/usr/bin/python3
""" Create a instance """

from flask import Flask


app = Flask(__name__)


""" Route for the homepage """


@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'


if __name__ == '__main__':
    """ Start the aplication on the port """
    app.run(host='0.0.0.0', port=5000)
