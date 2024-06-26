from flask import Flask, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import json

from Controller.Employee import Employees
from markupsafe import escape

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'company'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/<username>/employee')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

# Get all users
@app.route("/employees")
def employees():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    employee = Employees("", cursor)
    return employee.show_employees()


# Insert User to database
@app.route("/insert-user", methods=['POST'])
def insertuser():
    content = request.json
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO tbl_employees VALUES (NULL, %s, %s, %s)', (content['username'], content['email'], content['password']))
    mysql.connection.commit()

    cursor.execute('SELECT * FROM tbl_employees')
    users = cursor.fetchall()
    return json.dumps( users )



if __name__ == "__main__":
    app.run(debug=True)