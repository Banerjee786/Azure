# from flask import Flask
from flask import Flask, request, render_template
import os
import pypyodbc

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

'''
@app.route('/', methods=['POST'])
def my_form_post():
    if request.method== 'POST':
        range1 = request.form['text1']
        range2 = request.form['text2']
'''



if __name__ == '__main__':
  app.run()
