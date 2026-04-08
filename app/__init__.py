#imports
from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)