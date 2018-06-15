# from flask import Flask
from flask import Flask, request, render_template
import pypyodbc
import time


app = Flask(__name__)

server = 'banerjee.database.windows.net'
database = 'banerjeedb'
username = 'Priyam360'
password = 'Priyam555!'
driver = '{ODBC Driver 13 for SQL Server}'


@app.route('/')
def display():
    conn = pypyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()
    start = time.time()
    cursor.execute("SELECT top 10 * FROM equake where nst = 24")
    rows = cursor.fetchall()
    end = time.time()
    executiontime = end - start
    return render_template('searchearth.html', rows=rows, executiontime=executiontime)

if __name__ == '__main__':
  app.run()
