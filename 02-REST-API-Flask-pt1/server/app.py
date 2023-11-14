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

@app.route('/productions', methods=["GET", "POST"])
def showProductions():
    if request.method == "GET":
        productions = Production.query.all()
        all_productions = []
        for play in productions:
            all_productions.append(play.to_dict(only=('title', 'budget', 'genre', 'image', 'director', 'description', 'ongoing')))
        return make_response(all_productions, 200)
    elif request.method == "POST":
        data = request.get_json()
        new_production = Production(
            title = data["title"],
            genre = data["genre"],
            budget = data["budget"],
            image = data["image"],
            director = data["director"],
            description = data["description"],
            ongoing = data["ongoing"]
        )
        db.session.add(new_production)
        db.session.commit()
        return make_response(new_production.to_dict(), 201)
    return {}

#8. make a get, patch, and delete request to /productions/id, make responses and return a status code

@app.route('/productions/<id>', methods=["GET", "PATCH", "DELETE"])
def showProductionsById(id):
    production = Production.query.filter(Production.id == id).first()

    if production:
        if request.method == "PATCH":
            data = request.get_json()
            for attr in data:
                setattr(production, attr, data[attr])
            print(production.to_dict())
            db.session.add(production)
            db.session.commit()
            return make_response(production.to_dict(), 202)
        elif request.method == "DELETE":
            db.session.delete(production)
            db.session.commit()
            return make_response(production.to_dict(), 204)
        else:
            return make_response(production.to_dict(), 200)

    else:
        return make_response("Invalid request", 400)


# if __name__ == '__main__':
#     app.run(port=5555)