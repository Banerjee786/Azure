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


@app.route('/',methods=['GET','POST'])
def display():
    conn = pyodbc.connect('Driver=' + driver + ';Server=' + server + ';Database=' + database + ';UID=' + username + ';PWD=' + password +';')
    cursor = conn.cursor()
    SqlQuery = "SELECT * FROM [EQUAKE] WHERE latitude = 19.4088326 AND depth = 2.14"
    start = time.time()
    cursor.execute(SqlQuery)
    rows = cursor.fetchall()
    print(rows)
    end = time.time()
    executiontime = end - start
    cursor.close()
    conn.close()
    return render_template('searchearth.html', row=rows, executiontime=executiontime)


if __name__ == '__main__':
    app.run(debug=True)

