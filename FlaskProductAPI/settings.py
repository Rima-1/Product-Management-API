# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

# creating an instance of the flask app
app = Flask(__name__)

# configure our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False
