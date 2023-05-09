"""Models for whiteboard app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    notes = db.relationship("Note", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.username}>'


class Note(db.Model):
    """A note."""

    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(50))
    favorite = db.Column(db.Boolean, nullable=False)
    shared = db.Column(db.Boolean, nullable=False)

    user = db.relationship("User", back_populates="notes")

    def __repr__(self):
        return f'<Note note_id={self.note_id} title={self.title}>'
    

# class SharedNote(db.Model):
#     """A note that is shared between many users."""

#     note_id = db.Column(db.Integer, db.ForeignKey('notes.note_id'))





def connect_to_db(app):
    """Connect the database to Flask app"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///whiteboard"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)