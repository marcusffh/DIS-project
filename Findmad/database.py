from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2

db = SQLAlchemy() # we make an instance of SQLAlchemy to be able to handle database connections and such:)
bcrypt = Bcrypt() # Instance of Bcrypt for hashing passwords, which is basically encrypting the passwords for user safety
login_manager = LoginManager() # Instance of LoginManager which we use for handling login sessions


# PostgreSQL connection setup
conn = psycopg2.connect(
    dbname='recipe', # name of the database to connect to
    user='recipe',  # username for the database connection
    password='recipe', # password for the user
    host='localhost',  #Host where the database is located
    port=5433 # Connection port where the database is listening
) # Not like a mouse cursor, but a cursor in the sense that it lets us interact with the database
db_cursor = conn.cursor() # It lets usexecute quieres and so on