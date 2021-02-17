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

#_______________________________view functions for teacher login/registration___________________________________#

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
        # return jsonify({'status': 'ok', 'student_login_email': student_login_email})
        teacher_login_email = request.form.get('teacher_login_email')
        print(teacher_login_email)
        
        teacher=crud.get_teacher_by_email(teacher_login_email)
        session['teacher'] = {
            "teacher_id": teacher.teacher_id,
            "teacher_email": teacher.teacher_email,
            "teacher_fname": teacher.teacher_fname,
            'teacher_lname': teacher.teacher_lname,
            "teacher_phone": teacher.teacher_phone
            }
        print("!!!!!!!\nteacher\nIT'S HERE\n!!!!")
        print(teacher.teacher_email)
        print(session['teacher'])
        # return render_template('teacher-profile.html', email = teacher.teacher_email)
        return redirect('/teacher-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/teacher-portal-create', methods=["POST"])
def add_teacher():
    """Creates a teacher, adds the teacher to the teacher table"""
    teacher_fname = request.form.get('teacher_fname')
    teacher_lname = request.form.get('teacher_lname')
    teacher_email = request.form.get('teacher_email')
    teacher_phone = request.form.get('teacher_phone')
    teacher_password = request.form.get('teacher_password')

    # calls the crud function create_teacher()
    crud.create_teacher(teacher_fname, teacher_lname, teacher_email, teacher_phone, teacher_password)
    # return jsonify({new_teacher})
    # return new_teacher
    return jsonify({'status': 'ok', 'fname': teacher_fname, 'lname': teacher_lname})

#_______________________________view functions for student login/registration___________________________________#
@app.route('/student-portal')
def sign_up_student():
    """Renders the VMS sign-up page"""
    return render_template('student-portal.html')

@app.route('/student-portal', methods=["POST"])
def student_login():
    """Checks to see if email and password works, 
        
        redirects to personal profile with successful login"""

    student_login_email = request.form.get('student_login_email')
    student_login_pw = request.form.get('student_login_pw')

    checked_student = crud.verify_student(student_login_email, student_login_pw)

    if checked_student != None:
        # return jsonify({'status': 'ok', 'student_login_email': student_login_email})
        student_login_email = request.form.get('student_login_email')
        print(student_login_email)
        
        student=crud.get_student_by_email(student_login_email)
        session['student'] = {
            "student_id": student.student_id,
            "student_email": student.student_email,
            "student_fname": student.student_fname,
            'student_lname': student.student_lname,
            "private_teacher": student.private_teacher,
            "program_name": student.program_name,
            "instrument": student.instrument
            }
        print("!!!!!!!\nSTUDENT\nIT'S HERE\n!!!!")
        print(student.student_email)
        print(session['student'])
        # return render_template('student-profile.html', email = student.student_email)
        return redirect('/student-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/student-portal-create', methods=["POST"])
def add_student():
    """Creates a student, adds the student to the student table"""
    print("!!!!!!!!\nIM IN THE ADD STUDENT Function \n !!!!!!!!!!")
    student_fname = request.form.get('student_fname')
    student_lname = request.form.get('student_lname')
    student_email = request.form.get('student_email')
    private_teacher = request.form.get('private_teacher')
    program_name = request.form.get('program_name')
    instrument = request.form.get('instrument')
    student_password = request.form.get('student_password')

    crud.create_student(student_fname, student_lname, student_email, private_teacher, program_name, instrument, student_password)
    
    return redirect('/student-profile')
    # return jsonify({'status': 'ok', 'fname': student_fname, 'lname': student_lname})   

#___________________________________view functions for viewing profiles________________________________________#
@app.route('/student-profile')
def blank_student_profile():
    return render_template('student-profile.html')



@app.route('/teacher-profile')
def view_teacher_profile():
    """Renders the VMS teacher-profile page"""
    return render_template('teacher-profile.html')

#___________________________________functions for adding practice logs________________________________________#

@app.route('/practice-log')
def view_log_page():
    """Renders the VMS practice-log page"""
    return render_template('practice-log.html')

@app.route('/practice-log', methods=["POST"])
def add_log():
    """Creates a new log, adds the log to the log table"""
    print("****\nIM IN THE ADD LOG Function \n !!!!!!!!!!")
    log_date = request.form.get('log_date')
    log_start_time = request.form.get('log_start_time')
    log_end_time = request.form.get('log_end_time')
    log_pieces_practiced = request.form.get('log_pieces_practiced')
    log_practice_notes = request.form.get('log_practice_notes')
    student_id=session['student']['student_id']

    crud.create_log(log_date, student_id, log_start_time, log_end_time, log_pieces_practiced, log_practice_notes)
    
    # return redirect('/student-profile')
    return jsonify({'status': 'ok', 'log_date': log_date})  

#___________________________________functions for viewing logs________________________________________#
@app.route('/past-logs')
def view_logs_per_student():
    """View past logs for individual student"""
    return render_template('past-logs.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)