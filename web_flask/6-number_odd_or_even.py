#!/usr/bin/python3
""" Create a instance """

from flask import Flask, render_template


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

""" Route for the /C """


@app.route('/c/<text>', strict_slashes=False)
def disp_str(text):
    """ Replace underscore with space """
    text = text.replace('_', ' ')
    """ Returns C with formated str """
    return 'C {}'.format(text)

""" Route for the /python """


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text='is cool'):
    """ Replace underscore with space """
    text = text.replace('_', ' ')
    """ Return python """
    return 'Python {}'.format(text)

""" Route for /number/<n> """


@app.route('/number/<int:n>', strict_slashes=False)
def disp_num(n):
    """ Return number """
    return str(n) + ' is a number'

""" Route for the /number_template/<n> """


@app.route('/number_template/<int:n>', strict_slashes=False)
def disp_num_temp(n):
    """ Returns an HTML page only if n is integer """
    return render_template('5-number.html', n=n)

""" Route for the /number_odd_or_even/<n> """


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def disp_odd_or_even(n):
    """ Returns n is even|odd """
    return render_template('6-number_odd_or_even.html', n=n)

""" start the server """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
