from html import *
from jinja2 import *
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        if email.isspace() == False:
            if email.count("@") == 1 and email.count(".") == 1 and email.count(' ') < 0:
                return redirect('/welcome')
        return redirect('/')
                


        
        if password.count() >= 3 and password.count() <= 20:
            pass
            
    return redirect('/login')
        


@app.route("/welcome", methods=['POST', 'GET'])
def welcome(): 
    return render_template('welcome.html') 
   
@app.route("/")
def index():
    return render_template('functions.html')

app.run()