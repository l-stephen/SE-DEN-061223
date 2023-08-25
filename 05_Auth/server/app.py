# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 
# Standard imports/boilerplate setup (We added session)

# 7) import bcrypt here as well and wrap the app in bcrypt

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
#1. ✅ python -c 'import os; print(os.urandom(16))'
#Used to hash the session data
app.secret_key = b'\xb8C\xack"}]c_\xb7\xf0\xcdng\xe7\xdf'

# 2.✅ Create a Login route that will save a user to the session
    # 3.1 Create a login class that inherits from Resource
    # 3.2 Use api.add_resource to add the '/login' path
    # 3.3 Build out the post method
        # 3.3.1 convert the request from json and select the user name sent form the client. 
        # 3.3.2 Use the name to query the user with a .filter
        # 3.3.3 If found set the user_id to the session hash
        # 3.3.4 convert the user to_dict and send a response back to the client 

# 3. Create a logout route now! set session to None

# 4. Use @app.before_request, to run a function that checks if the session has the correct user, before every request


# 8) Create a route to sign in and authenticate the user




if __name__ == '__main__':
    app.run(port=5555)