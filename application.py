# print a nice greeting.
from flask import Flask, render_template, redirect, url_for, request

application = Flask(__name__)


# use decorators to link the function to a url
def home():
    return "Hello, World!"  # return a string


def data():
    return render_template('data.html')  # return a string


def welcome():
    return render_template('welcome.html')  # render a template


# route for handling the login page logic
def login():
    global error
    pass
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html')


methods = ['POST', 'GET']

application.add_url_rule('/', 'home', home)
application.add_url_rule('/data', 'data', data, methods=methods)
application.add_url_rule('/welcome', 'welcome', welcome)
application.add_url_rule('/login', 'login', login, methods=methods)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
