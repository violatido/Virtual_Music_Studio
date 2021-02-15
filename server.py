"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect, url_for, jsonify)
from model import connect_to_db 
import crud 
from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 


@app.route('/')
def create_homepage():
    """Renders the VMS homepage"""
    return render_template('homepage.html')


@app.route('/teacher-portal')
def show_teacher_reg_login_page():
    """Renders the Teacher registration/login page"""
    return render_template('teacher-portal.html')

@app.route('/teacher-portal', methods=["POST"])
def teacher_login():
    """Checks to see if email and password works"""
    teacher_login_email = request.form.get('teacher_login_email')
    teacher_login_pw = request.form.get('teacher_login_pw')

    checked_teacher = crud.verify_teacher(teacher_login_email, teacher_login_pw)

    if checked_teacher != None:
        flash('This works!')
        return redirect('/teacher-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/teacher-portal', methods=["POST"])
def add_teacher():
    """Creates a teacher, adds the teacher to the teacher table"""
    teacher_fname = request.form.get('teacher_fname')
    teacher_lname = request.form.get('teacher_lname')
    teacher_email = request.form.get('teacher_email')
    teacher_phone = request.form.get('teacher_phone')
    teacher_password = request.form.get('teacher_password')

    # calls the crud function create_teacher()
    crud.create_teacher(teacher_fname, teacher_lname, teacher_email, teacher_phone, teacher_password)

    return jsonify({'status': 'ok', 'fname': teacher_fname, 'lname': teacher_lname})


@app.route('/student-portal')
def sign_up_student():
    """Renders the VMS sign-up page"""
    return render_template('student-portal.html')

@app.route('/student-portal', methods=["POST"])
def student_login():
    """Checks to see if email and password works"""
    student_login_email = request.form.get('student_login_email')
    student_login_pw = request.form.get('student_login_pw')

    checked_student = crud.verify_student(student_login_email, student_login_pw)

    if checked_student != None:
        # return jsonify({'status': 'ok', 'student_login_email': student_login_email})
        return redirect('/student-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/student-portal', methods=["POST"])
def add_student():
    """Creates a student, adds the student to the student table"""

    student_fname = request.form.get('student_fname')
    student_lname = request.form.get('student_lname')
    student_email = request.form.get('student_email')
    private_teacher = request.form.get('private_teacher')
    program_name = request.form.get('program_name')
    instrument = request.form.get('instrument')
    student_password = request.form.get('student_password')

    # calls crud function create_student()
    crud.create_student(student_fname, student_lname, student_email, private_teacher, program_name, instrument, student_password)

    return jsonify({'status': 'ok', 'fname': student_fname, 'lname': student_lname})   


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