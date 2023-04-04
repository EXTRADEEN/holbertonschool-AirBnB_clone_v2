#!/usr/bin/python3
""" Create a instance """

from flask import Flask


app = Flask(__name__)


""" Route for the homepage """
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns Hello HBNB """
    return 'Hello HBNB!'

""" Route for the /hbnb """
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return 'HBNB'

""" start the server """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
