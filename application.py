# print a nice greeting.
from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response

value = {
    "mac_Id": "11:22:33:10:50:fg",
    "random_number1": 100,
    "random_number2": 47,
    "random_number3": 200,
    "random_number4": 92,
    "random_number5": 57,
    "random_number6": 212
}

application = Flask(__name__)


# use decorators to link the function to a url
def home():
    return "Hello, World!"  # return a string


def data():
    if request.method == 'GET':
        res = make_response(jsonify(value), 200)
        return res
    elif request.method == 'PUT':
        req = request.update_json()
        return req


def welcome():
    return render_template('welcome.html')  # render a template


def chart():
    return render_template('chart.html')


# route for handling the login page logic
def login():
    global error
    pass
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('chart'))
    return render_template('login.html')


methods = ['POST', 'GET', 'PUT']

application.add_url_rule('/', 'home', home)
application.add_url_rule('/welcome', 'welcome', welcome)
application.add_url_rule('/chart', 'chart', chart)
application.add_url_rule('/data', 'data', data, methods=['GET', 'PUT'])
application.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
