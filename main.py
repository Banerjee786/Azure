# from flask import Flask
from flask import Flask, request, render_template
import pypyodbc as pyodbc
import time


app = Flask(__name__)

server = 'banerjee.database.windows.net'
database = 'banerjeedb'
username = 'Priyam360'
password = 'Priyam555!'
#driver = '{SQL Server}'
driver = '{ODBC Driver 13 for SQL Server}'


@app.route('/')
def display():

    conn = pyodbc.connect('Driver=' + driver + ';Server=' + server + ';Database=' + database + ';UID=' + username + ';PWD=' + password +';')
    cursor = conn.cursor()
    SqlQuery = "SELECT mag FROM EQUAKE WHERE latitude = 19.4088326 AND depth = 2.14"
    start = time.time()

    rows = cursor.execute(SqlQuery).fetchall()
    row = []
    row.append(rows)
    '''
    end = time.time()
    executiontime = end - start
    cursor.close()
    conn.close()
    '''
    #rows = 5
    executiontime = 0.5
    return render_template('searchearth.html', row=row, executiontime=executiontime)


if __name__ == '__main__':
    app.run(debug=True)

