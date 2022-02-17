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

#creating new route for precipitation analysis
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#adding a route for our app that will allow this analysis to come to life. 
# But adding the stations route first   
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#creating a flask route for the temperature by month average
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#adding both the starting dates and end dates to a route so that we can calculate the descriptive statistics
#when copying the URL into the search bar, we'll need to add actual start and end dates in place of the "start" and "end" 
# in the specific URL in this format 2017-06-01/2017-06-30
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)



#notation for updating flask app
    #export FLASK_APP=app.py
    #set FLASK_APP=app.py
    #flask run
    