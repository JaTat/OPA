# the beginning of the api magic
import json
import mysql.connector
from mysql.connector import errorcode
import flask
from flask import request, url_for, jsonify
from flask_restful import Resource, Api
from datetime import datetime, date, timedelta
from dateutil import parser

app = flask.Flask(__name__)
api = Api(app)

# Home and errors ------------------------------
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Employee Database API Welcome</h1>
<p>A prototype API for the employee databas.</p>'''


@app.errorhandler(404)
def page_not_found(e, error=""):
    return error, 404


# Connection function ------------------------------


def connect(user, password, host, database):
    try:
        cnx = mysql.connector.connect(user=user, password=password,
                                      host=host,
                                      database=database)
        error = None
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            error = "Something is wrong with your user name or password"
            return [], error
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            error = "Database does not exist"
            return [], error
        else:
            error = err
            return [], error
    return cnx, error


# Classes ------------------------------

# GetTables
class GetTables(Resource):
    def __init__(self):
        self.user = 'root'
        self.password = 'w4sser'
        self.host = '127.0.0.1'
        self.database = 'employees'

    def get(self):
        # Connect to database including error handling
        cnx, err = connect(user=self.user, password=self.password,
                           host=self.host, database=self.database)
        if err is not None:
            return page_not_found(404, err)

        # initialize cursors
        cur = cnx.cursor(dictionary=True)
        # query
        cur.execute("SHOW TABLES")
        data = cur.fetchall()
        # close cursor and connection
        cur.close()
        cnx.close()
        return jsonify(data)


# GetColumns
class GetColumns(Resource):
    def __init__(self):
        self.user = 'root'
        self.password = 'w4sser'
        self.host = '127.0.0.1'
        self.database = 'employees'

    def get(self):
        query_parameters = request.args
        # get query parameters in this case table
        table = query_parameters.get('table')
        #table = 'employees'
        print(table)
        # query statement
        query = "SHOW columns FROM"

        if not (table):
            return page_not_found(404, "no table specified")

       # Connect to database including error handling
        cnx, err = connect(user=self.user, password=self.password,
                           host=self.host, database=self.database)

        if err is not None:
            return page_not_found(404, err)
        # initialize cursors
        cur = cnx.cursor(dictionary=True)

        cur.execute(query + " " + str(table))
        data = cur.fetchall()
        # close cursor and connection
        cur.close()
        cnx.close()
        return jsonify(data)

# GetEmployeeData


class GetEmployees(Resource):
    def __init__(self):
        self.user = 'root'
        self.password = 'w4sser'
        self.host = '127.0.0.1'
        self.database = 'employees'

    def get(self):
        query_parameters = request.args
        # get query parameters
        # start date
        hire_date_start = query_parameters.get('hire_date_start')
        # parse with error catching
        try:
            hire_date_start = parser.isoparse(hire_date_start)
        except:
            return page_not_found(404, "invalid start date")
        # end date
        hire_date_end = query_parameters.get('hire_date_end')
        try:
            hire_date_end = parser.isoparse(hire_date_end)
        except:
            return page_not_found(404, "invalid enddate")
        # parse wit erro catching
        #table = 'employees'
        # query statement
        query = "SELECT * FROM employees where hire_date BETWEEN DATE(%s) AND DATE(%s)"

       # Connect to database including error handling
        cnx, err = connect(user=self.user, password=self.password,
                           host=self.host, database=self.database)

        if err is not None:
            return page_not_found(404, err)
        # initialize cursors
        cur = cnx.cursor(dictionary=True)

        cur.execute(query, (hire_date_start, hire_date_end))
        data = cur.fetchall()
        # close cursor and connection
        cur.close()
        cnx.close()
        return jsonify(data)


# Resources ------------------------------

api.add_resource(GetTables, '/v1/tables')
api.add_resource(GetColumns, '/v1/columns')
api.add_resource(GetEmployees, '/v1/employees')


# if __name__ == '__main__':
#     app.run(port=5001, debug=True)
