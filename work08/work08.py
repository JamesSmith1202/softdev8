from flask import Flask, render_template, request, session, redirect, url_for

USERNAME = "yes"
PASSWORD = "no"

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")   
def root():
    if 'username' in session:
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if not 'username' in session:
        response = None
        errormessage = ""
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            if(username == USERNAME):
                if(password == PASSWORD):
                    session['username'] = username
                    return redirect(url_for('welcome'))
                else:
                    errormessage = "Incorrect password"
            else:
                errormessage = "Incorrect username and maybe password"
        return render_template('login.html', errormessage = errormessage)
    else:
        return redirect(url_for('welcome'))
    
@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
        return redirect(url_for('logout'))
    else:
        if not ('username' in session):
            return redirect(url_for('login'))
        else:
            return render_template('welcome.html', username = USERNAME)
    
@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template("logout.html", username = USERNAME)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()
