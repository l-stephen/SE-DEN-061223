#!/usr/bin/env python3

# 📚 Review With Students:
    # Creating and seeding models using SQLAlchemy, import model into app

# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5000
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' or flask db migrate -m "Created Tables"
        # flask db upgrade 
        # python seed.py

# RESTful Routing
# REST stands for Representational State Transfer 
# provides a way of mapping HTTP verbs (get, post, put, delete) and CRUD actions (create, read, update, delete) together. 
# It is a convention for defining routes and when something follows the rest principle it is known as RESTFUL.
# REST Reading: https://www.geeksforgeeks.org/restful-routes-in-node-js/ 

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Production

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

#Using routes we can add methods = [GET,POST] to our @app.route("/path")
#We can then check that the request.method == "GET" or "POST" or "DELETE" or "PATCH" and run our functionality
#When we post we can get the data by using request.form.get("field")
#Then we can make a response with make_response() and return a status code
# https://www.restapitutorial.com/httpstatuscodes.html 


#2. make a get and post request to /productions, make responses and return a status code
#demonstrate serialization



#8. make a get, patch, and delete request to /productions/id, make responses and return a status code
