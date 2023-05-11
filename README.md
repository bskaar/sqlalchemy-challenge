# sqlalchemy-challenge
Module 10 Challenge

Acknowledgements: Prof Ahmad Sweed for Week 10 Day 3 Activities that helped for me to clarify approach for Module 10 challenge.

All files are located in Repository sqlalchemy-challenge:

Part 1: Analyze and Exlore the Climate Data:

Please refer to repository Juptyer notebook: climate_starter.ipynb


Part 2: Design Your Climate App

Please refer to repository python file: app.py

Start server running app.py on Pythondata:

(base)
bruce@DESKTOP-U8EGKK1 MINGW64 ~/OneDrive/Desktop/Homework/sqlalchemy-challenge/SurfsUp (main)
$ conda activate pythondata
(pythondata)
bruce@DESKTOP-U8EGKK1 MINGW64 ~/OneDrive/Desktop/Homework/sqlalchemy-challenge/SurfsUp (main)
$ ls
Resources/  app.py  climate_starter.ipynb
(pythondata)
bruce@DESKTOP-U8EGKK1 MINGW64 ~/OneDrive/Desktop/Homework/sqlalchemy-challenge/SurfsUp (main)
$ python app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 911-579-121
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)



 Server activity for the below:

127.0.0.1 - - [11/May/2023 11:53:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/May/2023 11:53:58] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [11/May/2023 11:56:03] "GET /api/v1.0/precipitation HTTP/1.1" 200 -
127.0.0.1 - - [11/May/2023 11:57:04] "GET //api/v1.0/stations HTTP/1.1" 200 -
127.0.0.1 - - [11/May/2023 11:58:01] "GET //api/v1.0/tobs HTTP/1.1" 200 -
127.0.0.1 - - [11/May/2023 11:58:54] "GET /api/v1.0/2016-10-21 HTTP/1.1" 200 -
127.0.0.1 - - [11/May/2023 12:00:46] "GET /api/v1.0/2016-10-21/2016-10-31 HTTP/1.1" 200 -




1. Start at the homepage. (see Climate_app_Homepage.jpg in repository)

List all the available routes.

2. /api/v1.0/precipitation (see Climate_app_Precipitation.jpg in repository)

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

3. /api/v1.0/stations (see Climate_app_Stations.jpg in repository)

Return a JSON list of stations from the dataset.
4. /api/v1.0/tobs (see Climate_app_Tobs.jpg in repository)

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end> (see Climate_app_Start.jpg in repository) and (see Climate_app_Start_End.jpg in repository)

Note: to access either of the routes, you must know the start format yyyy-mm-dd and or start/end date in format yyyy-mm-dd/yyyy-mm-dd.

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.