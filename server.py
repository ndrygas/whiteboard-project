"""Server for whiteboard app."""

from flask import Flask

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    print(session)
    if "username" not in session:
        return render_template('homepage.html')
    
    else:
        username = session["username"]
        user = crud.get_user_by_name(username)
        return redirect(f"/{user.username}")
    
    

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
    """Log in a user and redirect to their notes."""

    username = request.form.get('username')
    password = request.form.get('password')
   
    user = crud.get_user_by_name(username)
    
    if user and user.password == password:
        session["username"] = user.username
        # flash(f"Successfully logged into {user.username}'s account.")
        return redirect(f"/{user.username}")
    else:
        flash("Please enter valid credentials or create a new account.")
        return redirect("/")
    

@app.route('/logout', methods=["POST"])
def log_out():
    """Log out a user and redirect to log in screen."""

    del session["username"]

    return redirect("/")
    

@app.route('/<username>')
def user_home(username):
    """Display a user's homepage and all of their active notes."""
    
    if "username" not in session:
        flash(f"You must be logged in to view your whiteboard.")
        return redirect("/")
    
    else:
        username = session["username"]
        user = crud.get_user_by_name(username)
        notes = crud.get_notes_by_user_id(user.user_id)
        shared = crud.get_shared_notes_by_user_id(user.user_id)
        shared_list = []
        for note in shared:
            note_obj = crud.get_note_by_id(note.note_id)
            shared_list.append(note_obj)
        print(shared)
        
        return render_template('note.html', user=user, notes=notes, shared=shared_list)


@app.route("/new-note", methods=["POST"])
def new_note():
    """Create a new note in a user's profile."""

    username = session["username"]
    print(username)
    user = crud.get_user_by_name(username)
    print(user)
    note = crud.create_note(user.user_id)
    db.session.add(note)
    print(crud.get_notes_by_user_id(user_id=user.user_id))
    db.session.commit()    

    return redirect(f"/{user.username}")


@app.route("/save-notes", methods=["POST"])
def update_note():
    """Save a user's progress on a note."""
    
    title = request.json.get("title")
    body = request.json.get("body")
    note_id = request.json.get("id")
    
    note = crud.get_note_by_id(note_id)
    crud.update_note(note.note_id, title, body)
    db.session.commit()
    
    return {"status": f"Note Saved"}


@app.route("/delete-note", methods=["POST"])
def delete_note():
    """Delete a user's note and remove it from shared notes in other user's whiteboards."""

    note_id = request.json.get("id")
    note = crud.get_note_by_id(note_id)
    db.session.delete(note)
    db.session.commit()

    return {"status": f"Note Deleted"}


@app.route("/share-note", methods=["POST"])
def share_note():
    """Share a note with another user."""

    note_id = request.json.get("id")
    username = request.json.get("user")
    note = crud.get_note_by_id(note_id)
    user = crud.get_user_by_name(username)
    print(user)

    if not user:
        return {"status": f"Error: No matching username, please try again."}
    
    elif user and user != None:
        #searches for a potential duplicate note in the database
        dupe_note = crud.get_shared_note_by_note_id_and_user_id(note_id, user.user_id)
        
        if dupe_note:
            #checks if the note has already been shared to this user, preventing duplicates
            return {"status": f"Note already shared"}
        else:
            #creates a new note share in the database
            new_share = crud.create_share(note_id=note.note_id, user_id=user.user_id)
            db.session.add(new_share)
            db.session.commit()
            return {"status": f"Note Share successful"}


@app.route("/remove-note", methods=["POST"])
def remove_note():
    """Remove a shared note from a user's whiteboard. 
       This does not delete the original note."""

    note_id = request.json.get("id")
    username = session["username"]
    user = crud.get_user_by_name(username)
    user_id = user.user_id

    note_user = crud.get_shared_note_by_note_id_and_user_id(note_id, user_id)

    db.session.delete(note_user)
    db.session.commit()

    return {"status": f"Note Removed"}



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)