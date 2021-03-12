"""Server for movie ratings app."""
import os
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db 
from datetime import datetime, timedelta
import crud 
from jinja2 import StrictUndefined 
from twilio.rest import Client


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 

#_________________________________homepage functions_____________________________________#

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
    """Checks to see if teacher's email and password is valid
    
    If the email/password combo is valid, the student is redirected to their profile page
    If invalid, error message is shown"""
    teacher_login_email = request.form.get('teacher_login_email')
    teacher_login_pw = request.form.get('teacher_login_pw')

    checked_teacher = crud.verify_teacher(teacher_login_email, teacher_login_pw)

    if checked_teacher:
        teacher_login_email = request.form.get('teacher_login_email')
        
        teacher=crud.get_teacher_by_email(teacher_login_email)
        session["teacher_id"]=teacher.teacher_id

        return redirect('/teacher-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/teacher-portal-create', methods=["POST"])
def add_teacher():
    """Creates a new teacher with an html form, 
    
    if form is valid, the function adds the teacher to the teacher table"""

    teacher_fname = request.form.get('teacher_fname')
    teacher_lname = request.form.get('teacher_lname')
    teacher_email = request.form.get('teacher_email')
    teacher_phone = request.form.get('teacher_phone')
    teacher_password = request.form.get('teacher_password')

    teacher = crud.create_teacher(teacher_fname, teacher_lname, teacher_email, teacher_phone, teacher_password)

    if teacher == None:
        return jsonify({'error': 'email already in use'})
    else: 
        return jsonify({'teacher_fname': teacher_fname, 'teacher_lname': teacher_lname})

#_______________________________view functions for student login/registration___________________________________#
@app.route('/student-portal')
def sign_up_student():
    """Renders the VMS sign-up page"""

    return render_template('student-portal.html')

@app.route('/student-portal', methods=["POST"])
def student_login():
    """Checks to see if student's email and password works, 
        
    If the email/password combo is valid, the student is redirected to their profile page
    If invalid, error message is shown"""

    student_login_email = request.form.get('student_login_email')
    student_login_pw = request.form.get('student_login_pw')

    checked_student = crud.verify_student(student_login_email, student_login_pw)

    if checked_student:
        student_login_email = request.form.get('student_login_email')
        
        student=crud.get_student_by_email(student_login_email)
        session["student_id"]=student.student_id

        return redirect('/student-profile')
    else:
        return jsonify({'status': 'error, login credentials incorrect'})

@app.route('/student-portal-create', methods=["POST"])
def add_student():
    """Creates a new student with an html form, 
    
    if form is valid, the function adds the student to the student table"""

    student_fname = request.form.get('student_fname')
    student_lname = request.form.get('student_lname')
    student_email = request.form.get('student_email')
    private_teacher_email = request.form.get('private_teacher_email')
    program_name = request.form.get('program_name')
    instrument = request.form.get('instrument')
    student_password = request.form.get('student_password')
    student_phone = request.form.get('student_phone')
    teacher = crud.get_teacher_by_email(private_teacher_email)

    student = crud.create_student(student_fname, student_lname, student_email, program_name, instrument, student_password, student_phone, teacher)

    if student:
        return jsonify({'student_fname': student_fname, 'student_lname': student_lname})
    else: 
        return jsonify({'status': 'error, registration credentials incorrect'})

#__________________________________________functions for viewing profiles__________________________________________#
@app.route('/student-profile')
def view_student_profile():
    """Renders the VMS student profile page
    
    Also updates the week displayed for student's weekly goals"""

    student = crud.get_student_by_id(session["student_id"])
    teacher = student.teacher
    private_teacher_email = request.form.get('private_teacher_email')


    return render_template('student-profile.html', student=student, teacher=teacher)

@app.route('/teacher-profile')
def view_teacher_profile():
    """Renders the VMS teacherprofile page"""

    teacher = crud.get_teacher_by_id(session["teacher_id"])
    # students = crud.get_students_by_teacher_id(teacher.teacher_id)

    return render_template('teacher-profile.html', teacher=teacher)

@app.route('/teacher-profile/<student_id>')
def go_to_student_profile(student_id):

    teacher = crud.get_teacher_by_id(session["teacher_id"])
    student = crud.get_student_by_id(student_id)    

    return render_template('student-profile.html', student=student, teacher=teacher)

@app.route('/teacher-profile-logs/<student_id>')
def go_to_student_logs(student_id):

    teacher = crud.get_teacher_by_id(session["teacher_id"])
    student = crud.get_student_by_id(student_id)
    student_logs = crud.get_logs_by_student_id(student_id)

    return render_template('charts.html', student= student, teacher=teacher, student_logs=student_logs)



#________________________________________functions for adding teacher notes________________________________________#
@app.route('/teacher-notes')
def view_teacher_notes():
    """Renders the VMS teacher notes page and note history"""

    teacher = crud.get_teacher_by_id(session["teacher_id"])
    teacher_notes= crud.get_notes_by_teacher_id(teacher.teacher_id)

    return render_template('teacher-notes.html', teacher=teacher, teacher_notes=teacher_notes)

@app.route('/teacher-notes', methods=["POST"])
def add_note():
    """Creates a new lesson note
    
    if the note form is valid, the session adds the note to the note table"""

    # remove
    # teacher = crud.get_teacher_by_id(session["teacher_id"])

    note_teacher_id = (session["teacher_id"])
    note_student_name = request.form.get('note_student_name')
    note_date = request.form.get('note_date')
    note_time = request.form.get('note_time')
    note_content = request.form.get('note_content')

    note = crud.create_note(note_teacher_id, note_student_name, note_date, note_time, note_content)
    
    return jsonify({'status': 'ok', 'note_date': note.note_date})  


#________________________________________functions for adding practice logs________________________________________#

@app.route('/practice-log')
def view_log_page():
    """Renders the VMS practice-log page with practice log form"""

    student = crud.get_student_by_id(session["student_id"])
    
    return render_template('practice-log.html', student=student)

@app.route('/practice-log', methods=["POST"])
def add_log():
    """Creates a new practice log
    
    if the log form is valid, the session adds the log to the log table"""

    #remove
    # student = crud.get_student_by_id(session["student_id"])

    log_student_id = (session["student_id"])
    log_date = request.form.get('log_date')
    log_minutes_practiced = request.form.get('log_minutes_practiced')
    log_pieces_practiced = request.form.get('log_pieces_practiced')
    log_practice_notes = request.form.get('log_practice_notes')
    
    log = crud.create_log(log_date, log_student_id, log_minutes_practiced, log_pieces_practiced, log_practice_notes)
    
    return jsonify({'status': 'ok', 'log_date': log_date})  

#___________________________________functions for viewing past logs by student id________________________________#
@app.route('/charts')
def view_student_logs():
    """Renders page for viewing past logs for individual student"""

    student = crud.get_student_by_id(session["student_id"])

    return render_template('charts.html', student=student)

@app.route('/charts/<student_id>')
def list_logs_by_student(student_id):
    """Lists every log made by a student depending on their student_id.
    
    All log info is passed into the HTML doc"""
    
    student = crud.get_student_by_id(student_id)
    student_logs=crud.get_logs_by_student_id(student.student_id)

    return render_template('charts.html', student= student, student_logs=student_logs)

#____________________________________functions for viewing/seeding data charts___________________________________#
@app.route('/charts/<student_id>')
def view_charts(student_id):
    """View data charts for practice logs"""
    return render_template('charts.html')

@app.route('/charts/1.json/<student_id>')
def seed_chart_one(student_id):
    """Passes data for minutes practiced and log dates into chart #1 as JSON"""

    if "student_id" in session:
        student_logs = crud.get_logs_by_student_id(student_id)
    elif "teacher_id" in session:
        teacher = crud.get_teacher_by_id(session["teacher_id"])
        valid_students = teacher.get_student_ids()
        
        if int(student_id) in valid_students:
            crud.get_logs_by_student_id
        else:
            return jsonify({"error": "student not valid"})

    # x-axis data: dates in the week
    practice_dates = [] # holds todays date and previous six days as list items
    date = datetime.now() # the date and time in this exact moment
    for _ in range(7):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        practice_dates.append(dater)
        date = date - timedelta(days=1) # first iteration = yesterday 

    minutes_practiced = []

    # y-axis data: minutes practiced on each date in the week
    for date in practice_dates: # loops over the dates of the week
        dates_practiced = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date(), student_id) #all practice dates 
        # dates_practiced = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date(), student.student_id) #all practice dates 
        if dates_practiced:
            minutes_practiced.append((date, dates_practiced.minutes_practiced))
        else:
            minutes_practiced.append((date, 0))
        
    data = {}
    data['dates_practiced'] = [datetime.strptime(date, "%Y-%m-%d").date().ctime()[4:10] for date, min_prac in minutes_practiced]
    #2021-02-28 21:05:57,764 INFO sqlalchemy.engine.base.Engine {'log_date_1': datetime.date(2021, 2, 23), 'param_1': 1}
    #<Log log_date=2021-02-22 student_id=4 log_id=6
    data['minutes_practiced'] = [min_prac for date, min_prac in minutes_practiced]
    #[('2021-2-28', 0), ('2021-2-27', 0), ('2021-2-26', 120), ('2021-2-25', 12), ('2021-2-24', 45), ('2021-2-23', 35), ('2021-2-22', 100)]

    return jsonify(data) 

@app.route('/charts/2.json/<student_id>')
def seed_chart_two(student_id):
    """ Passes data for days practiced over four weeks to chart #2 as JSON"""

    if "student_id" in session:
        student_logs = crud.get_logs_by_student_id(student_id)
    elif "teacher_id" in session:
        teacher = crud.get_teacher_by_id(session["teacher_id"])
        valid_students = teacher.get_student_ids()
        
        if int(student_id) in valid_students:
            crud.get_logs_by_student_id
        else:
            return jsonify({"error": "student not valid"})

    # x-axis data: dates in month (eventually divded into four weeks)
    dates_in_month = [] # holds todays date and previous 27 dates as list items
    date = datetime.now()
    for idx in range(28):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day) #formats each date
        dates_in_month.append(dater) #adds formatted date to dates_in_month list
        date = date - timedelta(days=1) #goes back a day from current date

    log_date = []

    # y-axis data: days practiced in each week of the month
    for date in dates_in_month: # loops over each date of the month
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date(), student_id) #finds and formatts all logged practice dates in DB
        if monthly_dates:
            log_date.append((date, 1)) #adds to log_date date in month, 1 to signify a practice session that date
        else:
            log_date.append((date, 0)) #adds date in month, 0 to signify no practice session that date

    data = {}
    data['dates_in_month'] = [datetime.strptime(date, "%Y-%m-%d").date().ctime()[4:10] for date, date_prac in log_date]
    data['log_date'] = [date_prac for date, date_prac in log_date]

    return jsonify(data) 

@app.route('/charts/3.json/<student_id>')
def seed_chart_three(student_id):
    """ Passes data for minutes practiced over four weeks to chart #3 as JSON"""

    if "student_id" in session:
        student_logs = crud.get_logs_by_student_id(student_id)
    elif "teacher_id" in session:
        teacher = crud.get_teacher_by_id(session["teacher_id"])
        valid_students = teacher.get_student_ids()
        
        if int(student_id) in valid_students:
            crud.get_logs_by_student_id
        else:
            return jsonify({"error": "student not valid"})


    # x-axis data: dates in month (eventually divded into four weeks)
    dates_in_month = [] # holds todays date and previous 27 dates as list items
    date = datetime.now()
    for idx in range(28):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day) #formats each date
        dates_in_month.append(dater) #adds formatted date to dates_in_month list
        date = date - timedelta(days=1) #goes back a day from current date

    minutes_practiced = []

    # note: use this var in 362 and 369
    # format_date = datetime.strptime(date, "%Y-%m-%d").date()

    # y-axis data: minutes practiced on each date in the month
    for date in dates_in_month: # loops over the dates of the month
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date(), student_id) #finds and formatts all logged practice dates in DB
        if monthly_dates:
            minutes_practiced.append((date, monthly_dates.minutes_practiced))
        else:
            minutes_practiced.append((date, 0))

    data = {}
    data['dates_in_month'] = [datetime.strptime(date, "%Y-%m-%d").date().ctime()[4:10] for date, date_prac in minutes_practiced]
    #['2021-3-1', '2021-2-28', '2021-2-27', '2021-2-26', '2021-2-25', '2021-2-24', '2021-2-23', '2021-2-22', '2021-2-21', '2021-2-20', '2021-2-19', '2021-2-18', '2021-2-17', '2021-2-16', '2021-2-15', '2021-2-14', '2021-2-13', '2021-2-12', '2021-2-11', '2021-2-10', '2021-2-9', '2021-2-8', '2021-2-7', '2021-2-6', '2021-2-5', '2021-2-4', '2021-2-3', '2021-2-2']
    data['minutes_practiced'] = [min_prac for date, min_prac in minutes_practiced]
    # [('2021-3-1', 45), ('2021-2-28', 0), ('2021-2-27', 0), ('2021-2-26', 120), ('2021-2-25', 12), ('2021-2-24', 45), ('2021-2-23', 35), ('2021-2-22', 100), ('2021-2-21', 22), ('2021-2-20', 0), ('2021-2-19', 45), ('2021-2-18', 22), ('2021-2-17', 23), ('2021-2-16', 45), ('2021-2-15', 0), ('2021-2-14', 10), ('2021-2-13', 0), ('2021-2-12', 72), ('2021-2-11', 0), ('2021-2-10', 42), ('2021-2-9', 0), ('2021-2-8', 50), ('2021-2-7', 65), ('2021-2-6', 35), ('2021-2-5', 122), ('2021-2-4', 40), ('2021-2-3', 25), ('2021-2-2', 0)]


    return jsonify(data) 

#_______________________________________functions for messaging__________________________________#
# @app.route('/message')
# def view_messages():
#     """View text messages"""

#     return render_template('message.html')

@app.route('/api/messages', methods=["POST"])
def send_message():
    """ Sends a text to a specific student from their teacher's profile page """

    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    student_id = request.form.get('phone_dropdown_id')

    student= crud.get_student_phone(student_id) # crud: return Student.query.filter(Student.student_id == student_id).first()
    
    student_num = student.student_phone "+1" + student_num


    text_message_content = request.form.get('message_content')
    # selecting a student id number

    message = client.messages.create(
                        body= text_message_content, #text message content here 
                        to=student_phone,
                        from_=os.environ["TWILIO_PHONE"]
                    )

    return jsonify({'message_content': text_message_content})


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)