from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()

    stephen = User(name="Stephen", password="password")
    test = User(name="test", password="test")
    db.session.add(stephen)
    db.session.add(test)
    db.session.commit()

