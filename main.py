from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        verify = request.form['verify']

        strikes = 0 
        pswd_ver = ""
        email_error = ""
        username_error = ""
        pswd_error = ""

        if len(password) < 3 or len(password) > 20 or " " in password:
            strikes += 1
            pswd_error = ("Invalid Password")
        
        if verify != password:
            strikes += 1
            pswd_ver = ("Password does not match")
           
        if len(username) < 3 or len(username) > 20 or " " in username:
            strikes += 1
            username_error = ("Username must be between 3 and 20 characters.")
        
        if email:
            if email.count('@') != 1 or email.count('.') != 1 or email.count(" ") > 0:
                strikes += 1
                email_error = ("Invalid Email Address")
        
        if strikes == 0:
            return redirect('/welcome?username=' + username)
        else:
            return render_template('functions.html', pswd_error=pswd_error, username_error=username_error, email_error=email_error, pswd_ver=pswd_ver, verify=verify, username=username, email=email)

    return render_template('functions.html')


@app.route("/welcome")
def welcome(): 
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()