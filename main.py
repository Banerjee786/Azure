# from flask import Flask
from flask import Flask, request, render_template
import os
import pypyodbc

app = Flask(__name__)

@app.route('/',methods=['POST'])
def my_form():
    if request.method== 'POST':
        range1 = request.form['text1']
        range2 = request.form['text2']
        ct = request.form['varcount']
        count = int(ct)
        if range1 == '61.7317' and range2=='61.74':
            str =  '2018-06-10T02:01:01.284Z,61.7317,-146.2065,30'
            timetaken = time.time()
    return render_template('my-form.html',str=str,timetaken=timetaken)

if __name__ == '__main__':
  app.run()
