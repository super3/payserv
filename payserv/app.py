import sqlite3
from flask import Flask


# Initialize the Flask application
app = Flask(__name__)
app.config['DATABASE'] = '/db/payserv.db'


# Database code
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])