#!/usr/bin/env python3
# 📚 Review With Students:
    # REST
    # Status codes
    # Error handling 
# Set up:
    # cd into server and run the following in the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5000
    # flask db init
    # flask db revision --autogenerate -m'Create tables' or flask db migrate -m "created tables"
    # flask db upgrade 
    # python seed.py
from flask import Flask, request, make_response, abort
from flask_migrate import Migrate
# 1.✅ Import NotFound from werkzeug.exceptions for error handling
#2. ✅ Import `Api` and `Resource` from `flask_restful`
    # ❓ What do these two classes do at a higher level? 
from werkzeug.exceptions import NotFound
from flask_restful import Api, Resource
from models import db, Production, CrewMember
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)


#3. Initialize the Api
    # `api = Api(app)`
api = Api(app)
#4. Create a Production class that inherits from Resource

class Productions(Resource):
#5. Create a GET (All) Route
    #Create a `productions` array.
    #Make a query for all productions. For each `production`, create a dictionary 
    # containing all attributes before appending to the `productions` array.
    #Create a `response` variable and set it to: 
    #  #make_response(
    #       jsonify(productions),
    #       200
    #  )
    #Return `response`.
    #After building the route, run the server and test in the browser.
    #Use our serializer to format our response to be cleaner

    def get(self):
        production_list = [p.to_dict() for p in Production.query.all()]
        response = make_response(
            production_list,
            200,
        )

        return response
 
#6. Create a POST Route.
    #Create a new production from the `request.form` object.
    #Add and commit the new production.
    #Convert the new production to a dictionary with `to_dict`
    #Set `make_response` to a `response` variable and pass it the new production along with a status of 201.
    #Test the route in Postman.

   
#7. Add the new route to our api with `api.add_resource`
    def post(self):
        new_production = Production(
            title=request.form['title'],
            genre=request.form['genre'],
            budget=int(request.form['budget']),
            image=request.form['image'],
            director=request.form['director'],
            description=request.form['description'],
            ongoing=bool(request.form['ongoing']),
        )

        db.session.add(new_production)
        db.session.commit()

        response_dict = new_production.to_dict()

        response = make_response(
            response_dict,
            201,
        )
        return response
api.add_resource(Productions, '/productions')

#8. Create a GET (One) route
    #Build a class called `ProductionByID` that inherits from `Resource`.
    #Create a `get` method and pass it the id along with `self`. (This is how we will gain access to 
    # the id from our request)
    #Make a query for our production by the `id` and build a `response` to send to the browser.


#9. Add the new route to our api with `api.add_resource`

#10. If a production is not found raise the NotFound exception
    #AND/OR use abort() to create a 404 with a customized error message
class ProductionByID(Resource):

    def get(self,id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            return handle_not_found(NotFound())
        
        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )
        
        return response
#11.Patch
    #Create a patch method that takes self and id
    #Query the Production from the id
    #If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    #Loop through the request.form object and update the productions attributes. Note: Be cautions of the data types to avoid errors.
    #add and commit the updated production 
    #Create and return the response

    def patch(self, id):
        production = Production.query.filter_by(id=id).first()

        if not production:
            abort(404, "The Production could not be found")

        data = request.get_json()
        for key in data:
            setattr(production, key, data[key])
        db.session.add(production)
        db.session.commit()

        production_dict = production.to_dict()

        response = make_response(
            production_dict, 200
        )

        return response
    
#12. Delete
    #Create a delete method, pass it self and the id
    #Query the Production 
    #If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    #delete the production and commit 
    #create a response with the status of 204 and return the response 
    def delete(self, id):
        production = Production.query.filter_by(id=id).first()

        if not production:
            abort(404, "The Production was not found")

        db.session.delete(production)
        db.session.commit()

        response = make_response("", 204)

        return response

   
api.add_resource(ProductionByID, '/productions/<int:id>')

#13. Use the @app.errorhandler() decorator to handle Not Found
    #Create the decorator and pass it NotFound
    #Use make_response to create a response with a message and the status 404
    #return the response
@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource was not found", 404)
    return response


# To run the file as a script
if __name__ == '__main__':
    app.run(port=4000, debug=True)
