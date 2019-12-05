from html import *
from jinja2 import *
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    user = request.form['username']
    if user == user:
        if user.count() <= 20 and user.count() >= 3:
            print('Username must be 3-20 charactes')
        elif " " in user:
            print("Invalid Username")
        return redirect("/welcome")
    return redirect ("/")

    pswd = request.form ['password']

    ver_pswd = request.form["password_confirmation"]
    if pswd == ver_pswd:
        return render_template
    else: 
        print("Password does not match.")
    

    email = request.form['email-address']

@app.route("/")
def index():
    return render_template('functions.html')

app.run()