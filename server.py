"""Server for whiteboard app."""

from flask import Flask

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
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

    print(username, password)

    if username != "" and password != "":
        user = crud.get_user_by_name(username)
        if user:
            flash("That username already exists. Please use a different name.")
        else:    
            user = crud.create_user(username, password)
            db.session.add(user)
            db.session.commit()
            initial_note = crud.create_note(user_id=user.user_id)
            db.session.add(initial_note)
            db.session.commit()
            flash("Success! Please log in.")
    else: 
        flash("Please fill in the create account form.")
        
        
    return redirect("/")


@app.route('/login', methods=["POST"])
def log_in():
    """Log in a user and redirect to their notes"""

    username = request.form.get('username')
    password = request.form.get('password')
    
   
    user = crud.get_user_by_name(username)
    if not user or user.password != password:
        flash("Please enter valid credentials or create a new account.")
        return redirect("/")
    else:
        session["username"] = user.username
        flash(f"Successfully logged into {user.username}'s account.")
        return redirect(f"/{user.username}")
    
   
    # try:
    #     if session[username] == password:
    #         return render_template('note.html')
    # except: 
    #     flash("Please enter valid credentials")
    #     return redirect("/notes")
    
@app.route('/<username>')
def user_home(username):
    
    username = session["username"]
    user = crud.get_user_by_name(username)
    # print(user)
    notes = crud.get_notes_by_user_id(user.user_id)
    # print(notes)
        
    return render_template('note.html', user=user, notes=notes)


@app.route("/update-note", methods=["POST"])
def update_note():
    
    title = request.form.get('title')
    body = request.form.get('body')
    note_id = request.form.get('note-id')
    print(note_id)
    username = session["username"]
    user = crud.get_user_by_name(username)    
    note = crud.get_note_by_id(note_id)

    crud.update_note(note.note_id, title, body)
    db.session.commit()
        
    return jsonify("note saved")

@app.route("/new-note", methods=["POST"])
def new_note():

    # title = request.form.get("title")
    username = session["username"]
    print(username)
    user = crud.get_user_by_name(username)
    print(user)
    note = crud.create_note(user.user_id)
    db.session.add(note)
    print(crud.get_notes_by_user_id(user_id=user.user_id))
    db.session.commit()    

    return redirect(f"/{user.username}")



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)