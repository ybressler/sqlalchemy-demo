import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Try getting the environment variable, else, get the default
DB_URI = os.environ.get('DB_URI','postgresql://postgres:@localhost:5432/postgres')

# This engine manages the connection to your database
engine = create_engine(DB_URI)

# This session maker allows you to establish a session which will transact with your database
session_maker = sessionmaker(bind=engine)

# Go ahead an make a session!
session = session_maker()

"""
Note: We'll only be using 1 session, for the sake of simplicity. Multiple sessions are
highly appropriate when multi-threading, parallel processing, or high-performance computing.
For more details on sessions, read here: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
"""
