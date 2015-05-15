import sqlite3
from flask import Flask


# Initialize the Flask application
app = Flask(__name__)
app.config['DATABASE'] = '/db/payserv.db'


# Database code
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# Routes
@app.route('/')
def index():
    return "Hello World"


# Run application
if __name__ == '__main__':
    # Run the Flask app
    app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True
    )