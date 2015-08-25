#!sweetEnv/bin/python
from app import app

app.run(debug=True)
#app.run(debug=True, host='0.0.0.0', port=5001)

# for setting up the MongoDB
from flask.ext.pymongo import PyMongo 

# PyMongo connects to the MongoDB server running on port 27017 
# on localhost, and assumes a default database name of app.name 
# (i.e. whatever name you pass to Flask). 
# This database is exposed as the db attribute.
mongo = PyMongo(app)
