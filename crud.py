"CRUD operations"

from model import db, User, Note, connect_to_db

def create_note(user_id, title, favorite=True, shared=False):
    """Create and return a new note."""

    note = Note(user_id=user_id, title=title, favorite=favorite, shared=shared)

    return note

def create_user(username, password):
    """Create and return a new user."""

    user = User(username=username, password=password)

    return user

if __name__ == "__main__":
    from server import app
    connect_to_db(app)