# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 
# Standard imports/boilerplate setup (We added session)

# 7) import bcrypt here as well and wrap the app in bcrypt
from flask_bcrypt import Bcrypt
from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, User
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)
CORS(app)
bcrypt = Bcrypt(app)
#1. ✅ python -c 'import os; print(os.urandom(16))'
#Used to hash the session data
app.secret_key = b'\\\xc2,\xc77\xb5\xf7\xb4\xed\xf2|o\x90U\xe7\xb8'

# 2.✅ Create a Login route that will save a user to the session
    # 3.1 Create a login class that inherits from Resource
    # 3.2 Use api.add_resource to add the '/login' path
    # 3.3 Build out the post method
        # 3.3.1 convert the request from json and select the user name sent form the client. 
        # 3.3.2 Use the name to query the user with a .filter
        # 3.3.3 If found set the user_id to the session hash
        # 3.3.4 convert the user to_dict and send a response back to the client 
class Users(Resource):
    def post(self):
        form_json = request.get_json()

        new_user = User(
            name = form_json['name'],
            password = form_json['password'],
        )
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        print(session['user_id'])
        return make_response(
            new_user.to_dict(), 201)
api.add_resource(Users, '/signup')


# 3. Create a logout route now! set session to None
class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            print(session['user_id'])
        return make_response({}, 204)
api.add_resource(Logout, '/logout')

# 4. Use @app.before_request, to run a function that checks if the session has the correct user, before every request
@app.before_request
def check_session():
    print(session)
    if session.get("user_id") is None:
        session["user_id"] = None
    else:
        print("User is logged in")
        print(session["user_id"])

# 8) Create a route to sign in and authenticate the user
class Login(Resource):
    def post(self):
        form_json = request.get_json()
        name = form_json["name"]
        password = form_json["password"]
        user = User.query.filter_by(name=name).first()
        if user and user.authenticate(password):
            session["user_id"] = user.id
            return make_response(user.to_dict(), 200)
        else:
            return make_response("Invalid Credentials", 401)
        
api.add_resource(Login, '/signin')

if __name__ == '__main__':
    app.run(port=5555)