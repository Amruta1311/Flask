import os   # Allows to grab directory names and file pathnames programmatically with python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   #pip install Flask-Migrate


basedir = os.path.abspath(os.path.dirname(__file__))    # __file-_ ==> basic.py. basedir contains the absolute path towards the file 'basic.py' is located to

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')   # This sets up the database location

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # We dont want to have to track every single modification in our DB for now in this case. Depends on the programmer

db = SQLAlchemy(app)    

Migrate(app, db)    #connects the app to the databse in order to add on migration capabilites to run those terminal commands

#The reason to use migrations is because the database is created and if we want to add a new column in the future it wint be easy without migration


#export FLASK_APP=basic.py      //Sets up the flask app
#flask db init                  //Initiate and set up the migrations directory
#flask db migrate -m "Cat"      //We create a migration command with a message to keep track of all the migration histories
#flask db upgrade               //This upgrades and performs the migrations for us

# Next time to update the databse we do the following:--
#flask db migrate -m "added breed column"
#flask db upgrade


# Lines 7,11,13,15 actually create a sequel like database for us purely through python 

##################################################################################

class Kitty(db.Model):      #Model is simply seting up a table in our database. Here we have passed in the model of the instance db

    __tablename__ = 'kitties'   # Manually overwritting a table name. Otherwise the table name created is named after the class defined

    id = db.Column(db.Integer, primary_key = True)      #id is a column defined for the table 'kitties' with unique entries of integer type permitted in each row of the column

    name = db.Column(db.Text)

    age = db.Column(db.Integer)

    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        
        self.name = name

        self.age = age

        self.breed = breed

    def __repr__(self):     # This gives the string representation of the object

        return f"Kitty {self.name} of the breed {self.breed} is {self.age} years old!"

