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
        connect_to_db(app)#, "postgresql:///whiteboard")

        # Create tables and add sample data
        db.create_all()
        test_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
    
    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"username": "nico", "password": "pico"},
                                  follow_redirects=True)
        self.assertIn(b"nico's Whiteboard", result.data)

        # self.tearDown()

        

    # def test_departments_list(self):
    #     """Test departments page."""

    #     result = self.client.get("/departments")
    #     self.assertIn(b"Legal", result.data)

    # def test_departments_details(self):
    #     """Test departments page."""

    #     result = self.client.get("/department/fin")
    #     self.assertIn(b"Phone: 555-1000", result.data)


# class FlaskTestsLoggedIn(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         app.config['SECRET_KEY'] = 'key'
#         self.client = app.test_client()

#         # Start each test with a user ID stored in the session.
#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['user_id'] = 1

#     def test_important_page(self):
#         """Test important page."""

#         result = self.client.get("/important")
#         self.assertIn(b"You are a valued user", result.data)


# class FlaskTestsLoggedOut(TestCase):
#     """Flask tests with no logged in user in session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         self.client = app.test_client()

#     def test_important_page(self):
#         """Test that user can't see important page when logged out."""

#         result = self.client.get("/important", follow_redirects=True)
#         self.assertNotIn(b"You are a valued user", result.data)
#         self.assertIn(b"You must be logged in", result.data)


if __name__ == "__main__":
    import unittest
    
    unittest.main()