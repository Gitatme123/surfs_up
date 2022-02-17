import datetime as dt
import numpy as np
import pandas as pd

#get the dependencies we need from SQLAlchemy, which will help us access our data in the SQLLite Database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#add the code to import the dependencies that we need for Flask
from flask import Flask, jsonify


#set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#save our references to each table. 
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database with this code
session = Session(engine)

#to define our Flask app, we are creating a Flask application called app
app = Flask(__name__)

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

#defining the welcome route
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')