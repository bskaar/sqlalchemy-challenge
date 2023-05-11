# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 1. import Flask
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(autoload_with=engine)

# Save reference to the table
measurement = base.classes.measurement
station = base.classes.station

#################################################
# Flask Setup
#################################################

#2. Create an app, being sure to pass_name_
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#3. Define what to do when a user hits the index route

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
)

@app.route("/api/v1.0/precipitation")
def names():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query the last 12 months of precipitation data
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    last_date = last_date[0]
    query_date = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= query_date).all()

# Convert the query results to a dictionary
    precipitation = []
    for result in results:
        row = {}
        row[result[0]] = result[1]
        precipitation.append(row)

    session.close()

# Return the JSON representation of dictionary
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

# Create our session (link) from Python to the DB
    session = Session(engine)


# Query all stations
    results = session.query(station.station, station.name).all()

    session.close()

# Return a JSON list of stations from the dataset
    stations = []
    for result in results:
        row = {}
        row["Station"] = result[0]
        row["Name"] = result[1]
        stations.append(row)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():

# Create our session (link) from Python to the DB
    session = Session(engine)

# Find the most recent date in the data set.
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    last_date = last_date[0]
    query_date = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)

# Query the dates and temperature observations of the most active station for the last year of data
    active_station = session.query(measurement.station).\
            group_by(measurement.station).\
            order_by(func.count(measurement.station).desc()).\
            first()
    active_station = active_station[0]
    results = session.query(measurement.date, measurement.tobs).\
            filter(measurement.station == active_station).\
            filter(measurement.date >= query_date).\
            all()

    session.close()
    
      # Return a JSON list of temperature observations (TOBS) for the previous year
    tobs_data = []
    for result in results:
        row = {}
        row[result[0]] = result[1]
        tobs_data.append(row)

    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).all()

    session.close()

    # Create a list of dictionaries containing TMIN, TAVG, and TMAX for the given start date
    start_temps = []
    for result in results:
        temp_dict = {}
        temp_dict["TMIN"] = result[0]
        temp_dict["TAVG"] = result[1]
        temp_dict["TMAX"] = result[2]
        start_temps.append(temp_dict)

    # Return the JSON representation of the list
    return jsonify(start_temps)


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the TMIN, TAVG, and TMAX for all dates between the start and end dates (inclusive)
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).filter(measurement.date <= end).all()

    session.close()

    # Create a list of dictionaries containing TMIN, TAVG, and TMAX for the given start and end dates
    start_end_temps = []
    for result in results:
        temp_dict = {}
        temp_dict["TMIN"] = result[0]
        temp_dict["TAVG"] = result[1]
        temp_dict["TMAX"] = result[2]
        start_end_temps.append(temp_dict)

    # Return the JSON representation of the list
    return jsonify(start_end_temps)


if __name__ == '__main__':
    app.run(debug=True)

