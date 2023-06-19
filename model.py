"""Models for whiteboard app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    notes = db.relationship("Note", secondary="notes_users", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.username}>'


class Note(db.Model):
    """A note."""

    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(50))
    body = db.Column(db.Text)

    user = db.relationship("User", secondary="notes_users", back_populates="notes")

    def __repr__(self):
        return f'<Note note_id={self.note_id} title={self.title}>'
    

class NoteUser(db.Model):
    """A user of a shared note. Many-to-many relationship with notes and users."""

    __tablename__ = 'notes_users'

    note_user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey("notes.note_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self):
        return f'''<NoteUser note_user_id={self.note_user_id} 
                note_id={self.note_id} user_id={self.user_id}>'''


def test_data():
    """Test data to verify accounts are working."""

    # Empty existing data
    NoteUser.query.delete()
    Note.query.delete()
    User.query.delete()
    
    # Sample users, notes, and note shares
    nico = User(username="nico", password="pico")
    wico = User(username="wico", password="lico")
    
    nico_note = Note(user_id=1, title="Title-1", body="Body-1")
    wico_note = Note(user_id=2, title="Title-2", body="Body-2")
    
    nico_share_to_wico = NoteUser(user_id=2, note_id=1)
    wico_share_to_nico = NoteUser(user_id=1, note_id=2)

    db.session.add_all([nico, wico])
    db.session.commit()
    db.session.add_all([nico_note, wico_note])
    db.session.commit()
    db.session.add_all([nico_share_to_wico, wico_share_to_nico])
    db.session.commit()


def connect_to_db(app):
    """Connect the database to Flask app"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///whiteboard"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)