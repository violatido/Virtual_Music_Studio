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

    if checked_teacher != None:
        teacher_login_email = request.form.get('teacher_login_email')
        
        teacher=crud.get_teacher_by_email(teacher_login_email)
        session["teacher_id"]=teacher.teacher_id

        return redirect('/teacher-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/teacher-portal-create', methods=["POST"])
def add_teacher():
    """Creates a new student with an html form, 
    
    if form is valid, the function adds the student to the student table"""

    teacher_fname = request.form.get('teacher_fname')
    teacher_lname = request.form.get('teacher_lname')
    teacher_email = request.form.get('teacher_email')
    teacher_phone = request.form.get('teacher_phone')
    teacher_password = request.form.get('teacher_password')

    crud.create_teacher(teacher_fname, teacher_lname, teacher_email, teacher_phone, teacher_password)
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

    if checked_student != None:
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
    private_teacher_name = request.form.get('private_teacher_name')
    private_teacher_email = request.form.get('private_teacher_email')
    program_name = request.form.get('program_name')
    instrument = request.form.get('instrument')
    student_password = request.form.get('student_password')
    teacher = crud.get_teacher_by_email(private_teacher_email)

    student = crud.create_student(student_fname, student_lname, student_email, program_name, instrument, student_password, teacher)

    return jsonify({'student_fname': student_fname, 'student_lname': student_lname})


#__________________________________________functions for viewing profiles__________________________________________#
@app.route('/student-profile')
def view_student_profile():
    """Renders the VMS student profile page"""

    student = crud.get_student_by_id(session["student_id"])
    teacher = student.teacher
    private_teacher_email = request.form.get('private_teacher_email')

    return render_template('student-profile.html', student=student, teacher=teacher)

@app.route('/teacher-profile')
def view_teacher_profile():
    """Renders the VMS teacherprofile page"""

    teacher = crud.get_teacher_by_id(session["teacher_id"])
    student = crud.get_student_by_id(session["student_id"])


    return render_template('teacher-profile.html', teacher=teacher, student=student)

@app.route('/teacher-profile/<student_id>')
def go_to_student_profile(student_id):


    teacher = crud.get_teacher_by_id(session["teacher_id"])
    student = crud.get_student_by_id(student_id)


    return render_template('student-profile.html', student=student, teacher=teacher)


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

    student = crud.get_student_by_id(session["student_id"])

    log_student_id = request.form.get('log_student_id')
    log_date = request.form.get('log_date')
    log_minutes_practiced = request.form.get('log_minutes_practiced')
    log_pieces_practiced = request.form.get('log_pieces_practiced')
    log_practice_notes = request.form.get('log_practice_notes')
    
    log = crud.create_log(log_date, log_student_id, log_minutes_practiced, log_pieces_practiced, log_practice_notes)
    
    return jsonify({'status': 'ok', 'log_date': log_date})  


#___________________________________functions for viewing past logs by student id________________________________#
@app.route('/past-logz')
def view_student_logs():
    """Renders page for viewing past logs for individual student"""

    student = crud.get_student_by_id(session["student_id"])


    return render_template('past-logs.html', student=student)

@app.route('/past-logs')
def list_logs_by_student():
    """Lists every log made by a student depending on their student_id.
    
    All log info is passed into the HTML doc"""
    student = crud.get_student_by_id(session["student_id"])
    student_logs=crud.get_logs_by_student_id(student.student_id)

    return render_template('past-logs.html', student= student, student_logs=student_logs)

#____________________________________functions for creating/seeding data charts____________________________________#
@app.route('/charts')
def view_charts():
    """View data charts for practice logs"""

    return render_template('charts.html')

@app.route('/charts.json')
def seed_chart_one():
    """Passes data for minutes practiced and log dates into chart #1 as JSON"""

    student = crud.get_student_by_id(session["student_id"])
    student_logs = crud.get_logs_by_student_id(student.student_id)

    # x-axis data: dates in the week
    practice_dates = [] # holds todays date and previous six days as list items
    date = datetime.now()
    for _ in range(7):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        practice_dates.append(dater)
        date = date - timedelta(days=1)

    #code unused
        # log_dates = [] 
        # log_minutes = [] 

        # for log in student_logs:
            #log_dates.append(log.log_date) #adds all practice dates to log_dates list
            #log_minutes.append(log.minutes_practiced) #adds all minutes practiced to minutes_practiced list

    minutes_practiced = []

    # y-axis data: minutes practiced on each date in the week
    for date in practice_dates: # loops over the dates of the week
        dates_practiced = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date()) #all practice dates 
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

@app.route('/charts/2.json')
def seed_chart_two():
    """ Passes data for days practiced over four weeks to chart #2 as JSON"""

    student = crud.get_student_by_id(session["student_id"])
    student_logs = crud.get_logs_by_student_id(student.student_id)

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
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date()) #finds and formatts all logged practice dates in DB
        if monthly_dates:
            log_date.append((date, 1)) #adds to log_date date in month, 1 to signify a practice session that date
        else:
            log_date.append((date, 0)) #adds date in month, 0 to signify no practice session that date

    data = {}
    data['dates_in_month'] = [datetime.strptime(date, "%Y-%m-%d").date().ctime()[4:10] for date, date_prac in log_date]
    data['log_date'] = [date_prac for date, date_prac in log_date]

    return jsonify(data) 


@app.route('/charts/3.json')
def seed_chart_three():
    """ Passes data for minutes practiced over four weeks to chart #3 as JSON"""

    student = crud.get_student_by_id(session["student_id"])
    student_logs = crud.get_logs_by_student_id(student.student_id)

    # x-axis data: dates in month (eventually divded into four weeks)
    dates_in_month = [] # holds todays date and previous 27 dates as list items
    date = datetime.now()
    for idx in range(28):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day) #formats each date
        dates_in_month.append(dater) #adds formatted date to dates_in_month list
        date = date - timedelta(days=1) #goes back a day from current date


    minutes_practiced = []

    # y-axis data: minutes practiced on each date in the month
    for date in dates_in_month: # loops over the dates of the month
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date()) #finds and formatts all logged practice dates in DB
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


@app.route('/charts/4.json')
def seed_chart_four():
    """ Passes data for days practiced per months over a year to chart #3 as JSON """

    student = crud.get_student_by_id(session["student_id"])
    student_logs = crud.get_logs_by_student_id(student.student_id)

    # x-axis data: dates in month (eventually divded into four weeks)
    dates_in_month = [] # holds todays date and previous 27 dates as list items
    date = datetime.now()
    for idx in range(28):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day) #formats each date
        dates_in_month.append(dater) #adds formatted date to dates_in_month list
        date = date - timedelta(days=1) #goes back a day from current date

    minutes_practiced = []
    # y-axis data: minutes practiced on each date in the month
    for date in dates_in_month: # loops over the dates of the month
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, "%Y-%m-%d").date()) #finds and formatts all logged practice dates in DB
        if monthly_dates:
            minutes_practiced.append((date, monthly_dates.minutes_practiced))
        else:
            minutes_practiced.append((date, 0))
    
    format_date = datetime.strptime(date, "%Y-%m-%d").date().ctime()[4:7] #Feb


    data = {}
    data['dates_in_month'] = [format_date for date, date_prac in minutes_practiced]
    #['2021-3-1', '2021-2-28', '2021-2-27', '2021-2-26', '2021-2-25', '2021-2-24', '2021-2-23', '2021-2-22', '2021-2-21', '2021-2-20', '2021-2-19', '2021-2-18', '2021-2-17', '2021-2-16', '2021-2-15', '2021-2-14', '2021-2-13', '2021-2-12', '2021-2-11', '2021-2-10', '2021-2-9', '2021-2-8', '2021-2-7', '2021-2-6', '2021-2-5', '2021-2-4', '2021-2-3', '2021-2-2']
    data['minutes_practiced'] = [min_prac for date, min_prac in minutes_practiced]

    return jsonify(data) 


#__________________________________functions for messaging__________________________________#
@app.route('/message')
def view_messages():
    """View text messages"""

    return render_template('message.html')

@app.route('/api/messages', methods=["POST"])
def send_message():
    """ Sends a text to user from submit button on message.html """

    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    # figure out how to get all the practice times and add them together per week
        # crud.get_practice_times(student_id)
        # just have the practice times -> add them all up (for loop)
        # return the amount of minutes practiced --> put it inside an f string

        # send out this message at a certain time - maybe sleeper function
    message = client.messages.create(
                        body= request.form.get('my-message'),
                        to=os.environ["MY_PHONE"],
                        from_=os.environ["TWILIO_PHONE"]
                    )

    messages = {}
    return jsonify(messages)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)