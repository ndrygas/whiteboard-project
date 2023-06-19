"""Script to seed database."""

import os

import model
import server

#Reset database, connect back to it, and create all tables within it

os.system("dropdb whiteboard")
os.system("createdb whiteboard")

model.connect_to_db(server.app)
model.db.create_all()
