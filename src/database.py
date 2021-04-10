from flask import current_app as app
from config import *
from flask_sqlalchemy import SQLAlchemy

# Setting up connection between app and db
db = SQLAlchemy(app)

# Setting up uri
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    

# Creating a database for storing patient names
class Patient(db.Model):
    """
    For storing patient name in the database

    """

    __tablename__ = "ENROLL PATIENT"
    sno = db.Column(db.INTEGER, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    age = db.Column(db.INTEGER, nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    cnumber = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(5000), nullable = False)
    date = db.Column(db.String(50), nullable = False)

    def __init__(self, name, age, gender, cnumber, desc, date):
        self.name = name
        self.age = age
        self.gender = gender
        self.cnumber = cnumber
        self.desc = desc
        self.date = date

    def ___repr__(self):
        return '<Users %r>' % self.name

# Created the database
db.create_all()