from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json
# from json import dumps

# Create a engine for connecting to SQLite3.
# Assuming titanic.db is in your app root folder

e = create_engine("sqlite:///titanic.db")

app = Flask(__name__)
api = Api(app)


class People_Meta(Resource):
    def get(self):
        # Connect to databse
        conn = e.connect()
        # Perform query and return JSON data
        query = conn.execute("select * from titanic")
        return json.dump({'people': [i for i in query.cursor.fetchall()]})


# class Departmental_Salary(Resource):
#     def get(self, department_name):
#         conn = e.connect()
#         query = conn.execute("select * from salaries where Department='%s'"%department_name.upper())
#         #Query the result and get cursor.Dumping that data to a JSON is looked by extension
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return result
#         #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


# api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(People_Meta, "/people")

if __name__ == "__main__":
    app.run()