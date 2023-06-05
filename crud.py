"CRUD operations"

from model import db, User, Note, NoteUser, connect_to_db

def create_user(username, password):
    """Create and return a new user."""

    user = User(username=username, password=password)
    
    return user


def get_user_by_id(user_id):
    """Return a user by using their primary key (ID)."""

    return User.query.get(user_id)


def get_user_by_name(username):
    """Return a user by using their username."""

    return User.query.filter(User.username == username).first()

def get_all_users():
    """Return all users."""

    return User.query.all()


def create_note(user_id, title="", body="", favorite=True):
    """Create and return a new note."""

    note = Note(user_id=user_id, title=title, body=body)

    return note


def get_note_by_id(note_id):
    """Return a note by its primary key (ID)."""

    return Note.query.get(note_id)


def get_notes_by_user_id(user_id):
    """Return all the notes made by a user, ordered by note ID."""

    return Note.query.filter_by(user_id=user_id).order_by("note_id").all()


def get_all_notes():
    """Returns all notes."""

    return Note.query.all()


def update_note(note_id, title, body):
    """Update the contents of a note."""

    note = Note.query.get(note_id)
    note.title = title
    note.body = body
    

def create_share(note_id, user_id):
    """Create a share for a note."""

    note_user = NoteUser(note_id=note_id, user_id=user_id)

    return note_user


def get_shared_notes_by_user_id(user_id):
    """Return all shared notes associated with a user ID."""

    return NoteUser.query.filter_by(user_id=user_id).order_by("note_id").all()


def get_shared_note_by_note_id_and_user_id(note_id, user_id):
    """Return a shared note by its primary key."""

    return NoteUser.query.filter_by(note_id=note_id, user_id=user_id).first()



if __name__ == "__main__":
    from server import app
    connect_to_db(app)