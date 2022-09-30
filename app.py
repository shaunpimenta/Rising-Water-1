from flask import Flask, render_template,request
from flaskwebui import FlaskUI
import os
from flask import Flask, flash, request, redirect, url_for, render_template,Response

app=Flask(__name__)
ui = FlaskUI(app, width=500, height=500)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/map')
def predict():
    return render_template('map1.html')
@app.route('/temp')
def temp():
    return render_template('temp.html')

if __name__=="__main__":
    # main()
    ui.run()
