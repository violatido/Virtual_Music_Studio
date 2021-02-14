"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db 
import crud 

from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 


# create view functions here
@app.route('/')
def create_homepage():
    """Renders the VMS homepage"""
    return render_template('homepage.html')

# @app.route('/')
# def check_login():
#     em = request.form['email']
#     pw = request.form['password']

@app.route('/sign-up')
def sign_up():
    """Renders the VMS sign-up page"""
    return render_template('sign-up.html')


@app.route('/student-profile')
def view_student_profile():
    """Renders the VMS student-profile page"""
    return render_template('student-profile.html')


@app.route('/teacher-profile')
def view_teacher_profile():
    """Renders the VMS teacher-profile page"""
    return render_template('teacher-profile.html')


@app.route('/practice-log')
def create_log():
    """Renders the VMS practice-log page"""
    return render_template('practice-log.html')
    

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)