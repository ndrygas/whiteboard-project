"""Tests for the app functions"""

from os import system
from unittest import TestCase
from server import app
from model import connect_to_db, db, test_data
from flask import session


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        system("dropdb whiteboard")
        system("createdb whiteboard")
        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app)

        # Create tables and add sample data
        db.create_all()
        test_data()
        

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    
    def test_login_and_notes(self):
        """Tests if user notes and shared notes are viewable on notes page."""

        result = self.client.post("/login",
                                  data={"username": "nico", "password": "pico"},
                                  follow_redirects=True)
        self.assertIn(b"nico's Whiteboard", result.data)
        self.assertIn(b"Title-1", result.data)
        self.assertIn(b"Title-2", result.data)


    #test logged out while trying to view user page
    def test_redirects_to_login(self):
        """Test if app redirects to login page when trying to view notes
        while not logged in."""

        result = self.client.get("/nico", follow_redirects=True)
        self.assertIn(b"You must be logged in to view your whiteboard", result.data)
        


if __name__ == "__main__":
    import unittest
    unittest.main()