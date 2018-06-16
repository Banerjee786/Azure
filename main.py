# from flask import Flask
from flask import Flask, request, render_template
import pyodbc
import time
import matplotlib


app = Flask(__name__)

server = 'tcp:banerjee.database.windows.net'
database = 'banerjeedb'
username = 'Priyam360@banerjee'
password = '**********'
#driver = '{SQL Server}'
driver = '{ODBC Driver 13 for SQL Server}'


@app.route('/')
def display():
    conn = pyodbc.connect('Driver=' + driver + ';Server=' + server + ';Port=1433;Database=' + database + ';UID=' + username + ';PWD=' + password +';')
    cursor = conn.cursor()
    SqlQuery = "SELECT * FROM [EQUAKE] WHERE depth = 2.14"
    start = time.time()
    cursor.execute(SqlQuery)
    #rows = cursor.fetchall()
    end = time.time()
    executiontime = end - start
    cursor.close()
    conn.close()
    return render_template('searchearth.html', executiontime=executiontime)


if __name__ == '__main__':
    app.run(debug=True)

