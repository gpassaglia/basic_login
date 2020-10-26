from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response, flash

from forms import LoginForm

from config import Config

application = Flask(__name__)
application.config.from_object(Config)


def home():
    return "Hello, World!"  # return a string


def welcome():
    return render_template('welcome.html')  # render a template


def chart():
    return render_template('chart.html')


# route for handling the login page logic
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('chart'))
    return render_template('login.html', title='Sign In', form=form)


methods = ['POST', 'GET', 'PUT']

application.add_url_rule('/', 'home', home)
application.add_url_rule('/welcome', 'welcome', welcome)
application.add_url_rule('/chart', 'chart', chart)
application.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
