# from flask import Flask
from flask import Flask, request, render_template
import pyodbc
import time
import matplotlib


app = Flask(__name__)

server = 'tcp:banerjee.database.windows.net'
database = 'banerjeedb'
username = 'Priyam360@banerjee'
password = 'Priyam555!'
#driver = '{SQL Server}'
driver = '{ODBC Driver 13 for SQL Server}'


@app.route('/')
def display():
    conn = pyodbc.connect('Driver=' + driver + ';Server=' + server + ';Port=1433;Database=' + database + ';UID=' + username + ';PWD=' + password +';')
    cursor = conn.cursor()
    SqlQuery = "SELECT * FROM [EQUAKE] WHERE depth = 2.14"
    start = time.time()
    cursor.execute(SqlQuery)
    rows = cursor.fetchall()
    print(rows[0])
    end = time.time()
    executiontime = end - start
    cursor.close()
    conn.close()
    return rows[0]
    #return render_template('searchearth.html', rows=rows, executiontime=executiontime)


if __name__ == '__main__':
    app.run(debug=True)

