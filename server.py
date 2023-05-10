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

@app.route("/create-account", methods=["POST"])
def create_account():
    """Create a new user account and redirect back to login page"""
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username != None and password !=None:
        try:
            user = crud.get_user_by_name(username)
            if user:
                flash("That username already exists. Please use a different name.")
        except:
    
            
                user = crud.create_user(username, password)
                db.session.add(user)
                db.session.commit()
                flash("Success! Please log in.")
    # else: 
    #     flash("Please fill in the create account form.")
        
        
    return redirect("/")

@app.route('/login', methods=["POST"])
def log_in():
    """Log in a user and redirect to their notes"""

    username = request.form.get('username')
    password = request.form.get('password')
   
    
   
    try:
        if session[username] == password:
            return render_template('note.html')
    except: 
        flash("Please enter valid credentials")
        return redirect("/")
    
# @app.route('/notes', methods=["POST"])
# def user_home():
    

    # return render_template('note.html')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)