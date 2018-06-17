# from flask import Flask
from flask import Flask, request, render_template, redirect
import pyodbc
import time
import datetime
import os



app = Flask(__name__)

server = 'banerjee.database.windows.net'
database = 'banerjeedb'
username = 'Priyam360'
password = 'Priyam555!'
#driver = '{SQL Server}'
driver = '{ODBC Driver 13 for SQL Server}'


@app.route('/')
def display():
    conn = pyodbc.connect('Driver=' + driver + ';Server=' + server + ';Port=1433;Database=' + database + ';UID=' + username + ';PWD=' + password +';')
    cursor = conn.cursor()
    start = time.time()
    SqlQuery = "SELECT TOP 10 * FROM [EQUAKE]"
    cursor.execute(SqlQuery)
    rows = cursor.fetchall()
    end = time.time()
    executiontime = end - start
    return render_template('searchearth.html', rows=rows, executiontime=executiontime)


if __name__ == '__main__':
    app.run(debug=True)

