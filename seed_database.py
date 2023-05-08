"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("pg_dump whiteboard > whiteboard.sql")
os.system("dropdb whiteboard")
os.system("createdb whiteboard")

model.connect_to_db(server.app)
model.db.create_all()
