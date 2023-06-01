"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

#Reset database, connect back to it, and create all tables within it

# os.system("pg_dump whiteboard > whiteboard.sql")
os.system("dropdb whiteboard")
os.system("createdb whiteboard")
# os.system("psql whiteboard < whiteboard.sql")
model.connect_to_db(server.app)
model.db.create_all()

# test_user = crud.create_user(username='nico', password='pico')

# model.db.session.add(test_user)
# model.db.session.commit()
