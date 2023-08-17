from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
#Review: Serializer rules, validations
db = SQLAlchemy()
#There are many ways to include constraints in models
#db.CheckConstraint
#nullable = False
#unique = True
#@validates('')

class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    # 1.✅ Add Constraints to the Columns 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    crew_members = db.relationship('CrewMember', backref='production')
 
        
    # serialize_rules = ('-crew_members.production',)
    serialize_rules = ('-crew_members', '-created_at', '-updated_at',)
    #add a validation using @validates()
    @validates('title')
    def validate_title(self, key, value):
        if not value:
            raise ValueError("Title cannot be empty")
        return value
    
    # 2.✅ Use the "validates" decorator to create a validation for images
    # 3.1 Pass the decorator 'image'
    # 3.2 Define a validate_image method, pass it self, key and image_path
    # 3.3 If .jpg is not in the image passed, raise the ValueError exceptions else 
    # return the image_path
    # Note: Feel free to try out more validations! 
    @validates('image')
    def validate_image(self, key, image_path):
        if '.jpg' not in image_path:
            raise ValueError("Image path must contain a .jpg extension")
        return image_path

    # 3.✅ navigate to app.py

    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'

class CrewMember(db.Model, SerializerMixin):
    __tablename__ = 'crew_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    
    # serialize_rules = ('-production.crew_members',)
    serialize_rules = ('-production',)
    #add a validation using @validates( )
    @validates('role')
    def validate_role(self, key, value):
        if not value:
            raise ValueError("Role cannot be empty")
        return value
    
    def __repr__(self):
        return f'<Production Name:{self.name}, Role:{self.role}'

