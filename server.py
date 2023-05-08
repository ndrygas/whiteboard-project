"""Server for whiteboard app."""

from flask import Flask

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/login', methods=["POST"])
def user_home():
    """Log in a user and redirect to their notes"""

    session['nico'] = 'pico'

    username = request.form.get('username')
    print(username)
    password = request.form.get('password')
    print(password)

    if session[username] == password:
        return render_template('note.html')

    # return render_template('note.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)