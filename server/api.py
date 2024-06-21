from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import json

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'company'

# Intialize MySQL
mysql = MySQL(app)

# Get all users
@app.route("/employees")
def employees():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tbl_employees')
    users = cursor.fetchall()
    return json.dumps( users )

# Insert User to database
@app.route("/insert-user")
def insertuser():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO tbl_employees VALUES (NULL, %s, %s, %s)', ('dave', '123', 'dave@gmail.com'))
    mysql.connection.commit()
    return 'You have successfully registered!'



if __name__ == "__main__":
    app.run(debug=True)