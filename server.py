"""Server for Virtual Music Studio app."""
import os
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, Student, Teacher
from datetime import datetime, timedelta
import crud
from jinja2 import StrictUndefined
from twilio.rest import Client

#import custom func for hashing
from utils.cipher import hash_input

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
connect_to_db(app)

#____________________________________________homepage functions_________________________________________________#

@app.route('/')
def create_homepage():
    """Renders the VMS homepage"""
    return render_template('homepage.html')


#__________________________________view functions for teacher login/registration___________________________________#


@app.route('/teacher-portal', methods=["GET", "POST"])
def teacher_login():
    """
    Renders the Teacher registration/login page

    _OR_

    Checks to see if teacher's email and password is valid

    If the email/password combo is valid, the student is redirected to their profile page
    If invalid, error message is shown
    """

    # If the teacher didn't try to sign in
    if not request.form:
        return render_template('teacher-portal.html')

    # Otherwise, try signing them in
    teacher_login_email = request.form.get('teacher_login_email')
    teacher_login_pw = request.form.get('teacher_login_pw')
    
    # if data is empty, do nothing
    if not all([teacher_login_email, teacher_login_pw]):
        return render_template('teacher-portal.html')

    #  No need to do it twice since you've already gotten this teacher
    my_teacher = crud.verify_teacher(teacher_login_email, hash_input(teacher_login_pw))

    if my_teacher:
        session['teacher_id'] = my_teacher.teacher_id
        return redirect('/teacher-profile')
    else:
        return jsonify({'status': 'error'})

@app.route('/teacher-portal-create', methods=["POST"])
def add_teacher():
    """Creates a new teacher with an HTML form,

    if form is valid, the function adds the teacher to the teacher table

    """

    teacher_fname = request.form.get('teacher_fname')
    teacher_lname = request.form.get('teacher_lname')
    teacher_email = request.form.get('teacher_email')
    teacher_phone = request.form.get('teacher_phone')
    teacher_password = request.form.get('teacher_password')

    # check to see if teacher already exists
    # more explicit, less complicated: get the first teacher that has the email
    teacher = db.session.query(Teacher).filter(Teacher.teacher_email == teacher_email).first()

    if teacher:
        return jsonify({'status': 'error- email already in use'})

    # now create the teacher:
    teacher = crud.create_teacher(teacher_fname, teacher_lname, teacher_email, teacher_phone, hash_input(teacher_password))

    if not teacher: 
        return jsonify({'status': 'error-please try again'})

    return jsonify({'status': 'ok', 'full_name':teacher.full_name, 'email':teacher.teacher_email, 'pw':teacher.teacher_password})
        

@app.route('/teacher-logout')
def teacher_logout():

    if session['teacher_id']:
        session.pop('teacher_id')
        return redirect('/')

    else:
        session.clear()

#_______________________________view functions for student login/registration___________________________________#

@app.route('/student-portal', methods=["GET", "POST"])
def student_login():
    """
    Renders the VMS sign-up page

    _OR_

    Checks to see if student's email and password works,

    If the email/password combo is valid, the student is redirected to their profile page
    If invalid, error message is shown
    """

    if not request.form:
        return render_template('student-portal.html')


    student_login_email = request.form.get('student_login_email')
    student_login_pw = request.form.get('student_login_pw')

    # if data is empty, do nothing
    if not all([student_login_email, student_login_pw]):
        return render_template('student-portal.html')

    my_student = crud.verify_student(student_login_email, hash_input(student_login_pw))

    if my_student:
        session['student_id'] = my_student.student_id
        return redirect('/student-profile')

    else:
        return jsonify({'status': 'error, login credentials incorrect'})

@app.route('/student-portal-create', methods=['POST'])
def add_student():
    """
    Creates a new student with an html form,
    if form is valid, the function adds the student to the student table
    """

    print('********' * 10, 'before forms')

    student_fname = request.form.get('student_fname')
    student_lname = request.form.get('student_lname')
    student_email = request.form.get('student_email')
    private_teacher_email = request.form.get('private_teacher_email')
    program_name = request.form.get('program_name')
    instrument = request.form.get('instrument')
    student_password = request.form.get('student_password')
    student_phone = request.form.get('student_phone')

    # check if student already exists
    student = db.session.query(Student).filter(Student.student_email == student_email).first()
    
    if student:
        return jsonify({'status': 'error- email already in use'})

    # verify that teacher exists:
    teacher = crud.get_teacher_by_email(private_teacher_email)
    if not teacher:
        return ({'status': 'error- no teacher in database'})
    
    # create the student
    student = crud.create_student(student_fname, student_lname, student_email, program_name, instrument, hash_input(student_password), student_phone, teacher.teacher_id)
    if not student:
        return jsonify({'status': 'error-please try again'})
    
    return jsonify({'status': 'ok', 'full_name':student.full_name, 'email':student.student_email, 'pw':student.student_password})


@app.route('/student-logout')
def student_logout():

    if session['student_id']:
        session.pop('student_id')
        return redirect('/')
    else:
        session.clear()


#__________________________________________functions for profiles__________________________________________#
@app.route('/student-profile', methods=["GET", "POST"])
def view_student_profile():
    """Renders the VMS student profile page"""

    if 'student_id' not in session:
        return jsonify({'error':'No student_id in session. Please log in!'})

    student = crud.get_student_by_id(session['student_id'])
    teacher = student.teacher

    return render_template('student-profile.html', student = student, teacher = teacher)


@app.route('/teacher-profile')
def view_teacher_profile():
    """Renders the profile page for the teacher in session"""

    if 'teacher_id' not in session:
        return jsonify({'error':'No teacher_id in session. Please log in!'})

    teacher = crud.get_teacher_by_id(session['teacher_id'])

    return render_template('teacher-profile.html', teacher = teacher)

@app.route('/teacher-profile/<student_id>')
def go_to_student_profile(student_id):
    """ Allows a teacher to see each of their students's profile page"""

    teacher = crud.get_teacher_by_id(session['teacher_id'])
    student = crud.get_student_by_id(student_id)

    return render_template('student-profile.html', student = student, teacher = teacher)

@app.route('/teacher-profile-logs/<student_id>')
def go_to_student_logs(student_id):
    """ Lets a teacher see each of their students's practice log history and data"""

    teacher = crud.get_teacher_by_id(session['teacher_id'])
    student = crud.get_student_by_id(student_id)

    # Get the student's logs through the relationship
    student_logs = student.logs

    return render_template('charts.html', student = student, teacher=teacher, student_logs = student_logs)

#______________________________________functions for adding teacher notes________________________________________#
@app.route('/teacher-notes', methods=['GET', 'POST'])
def add_note():
    """
    Renders the VMS teacher notes page and note history

    _OR_

    Creates a new lesson note

    if the note form is valid, the session adds the note to the note table
    """

    if not request.form:
        teacher = crud.get_teacher_by_id(session['teacher_id'])
        teacher_notes = teacher.notes

        return render_template('teacher-notes.html', teacher = teacher, teacher_notes = teacher_notes)

    note_teacher_id = (session['teacher_id'])
    student_id = request.form.get('note_student_name')
    note_date = request.form.get('note_date')
    note_time = request.form.get('note_time')
    note_content = request.form.get('note_content')

    # Combine date and time to parse provided objects into a datetime object
    note_created_at = datetime.strptime(note_date + ' ' + note_time, '%Y-%m-%d %H:%M')

    note = crud.create_note(note_teacher_id, student_id, note_created_at, note_content)
    
    return jsonify({'status': 'ok', 'note_date': note.note_created_at})

#______________________________________functions for adding practice logs________________________________________#

@app.route('/practice-log', methods=["GET", "POST"])
def view_log_page():
    """
    Renders the VMS practice-log page with practice log form

    _OR_

    Creates a new practice log

    if the log form is valid, the session adds the log to the log table

    """

    if not request.form:
        return jsonify({'status':'error', 'log_date':None})

    log_student_id = (session['student_id'])
    log_date = request.form.get('log_date')
    log_minutes_practiced = request.form.get('log_minutes_practiced')
    log_pieces_practiced = request.form.get('log_pieces_practiced')
    log_practice_notes = request.form.get('log_practice_notes')

    log = crud.create_log(log_date, log_student_id, log_minutes_practiced, log_pieces_practiced, log_practice_notes)

    return jsonify({'status': 'ok', 'log_date': log_date})

#____________________________________functions for viewing past logs by student id________________________________#
@app.route('/charts')
def view_student_logs():
    """Renders page for viewing past logs for individual student"""

    student = crud.get_student_by_id(session['student_id'])
    teacher = crud.get_teacher_by_id(session["teacher_id"])

    return render_template('charts.html', student=student, teacher=teacher)

@app.route('/charts/<student_id>')
def list_logs_by_student(student_id):
    """Lists every log made by a student depending on their student_id."""

    student = crud.get_student_by_id(student_id)
    student_logs = student.logs

    if "teacher_id" in session:
        teacher = crud.get_teacher_by_id(session["teacher_id"]) 
    else:
        teacher = None

    return render_template('charts.html', student= student, teacher=teacher, student_logs=student_logs)

#____________________________________functions for viewing/seeding data charts___________________________________#
@app.route('/charts/<student_id>')
def view_charts(student_id):
    """View data charts for practice logs"""
    return render_template('charts.html')

@app.route('/charts/1.json/<student_id>')
def seed_chart_one(student_id):
    """
    Passes data for minutes practiced and log dates into chart #1 as JSON

    """

    if not student_id:
        raise ValueError(f'{student_id=}')

    if type(student_id) != int:
        student_id=int(student_id)


    if "student_id" in session:
        pass

    elif "teacher_id" in session:

        # Get the student in one query
        my_student = db.session.query(Student)\
            .join(Teacher)\
            .filter(
                Teacher.teacher_id==session['teacher_id'],
                Student.student_id==student_id
            )\
            .first()

        if my_student:
            # Get the logs from the relationship
            stu_logs = my_student.logs

        else:
            return jsonify({'error': 'student not valid'})

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # YB: Consider utilizing pandas here to group by an interval.
    # Pandas is excelent at time series data. You could [bin] your data by week/month/etc

    # x-axis data: dates in the week
    practice_dates = [] # holds todays date and previous six days as list items
    date = datetime.now()
    for _ in range(7):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        practice_dates.append(dater)
        date = date - timedelta(days=1) # ex: first iteration = yesterday

    minutes_practiced = []

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


    # y-axis data: minutes practiced on each date in the week
    for dt in practice_dates: # loops over the dates of the week
        dates_practiced = crud.search_logs_by_date(datetime.strptime(dt, '%Y-%m-%d').date(), student_id) #all practice dates

        if dates_practiced:
            minutes_practiced.append((dt, dates_practiced.minutes_practiced))
        else:
            minutes_practiced.append((dt, 0))

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    data = {}
    data['dates_practiced'] = [datetime.strptime(dt, '%Y-%m-%d').date().ctime()[4:10] for dt, min_prac in minutes_practiced]
    #2021-02-28 21:05:57,764 INFO sqlalchemy.engine.base.Engine {'log_date_1': datetime.date(2021, 2, 23), 'param_1': 1}
    data['minutes_practiced'] = [min_prac for dt, min_prac in minutes_practiced]
    #[('2021-2-28', 0), ('2021-2-27', 0), ('2021-2-26', 120), ('2021-2-25', 12), ('2021-2-24', 45), ('2021-2-23', 35), ('2021-2-22', 100)]


    return jsonify(data)



@app.route('/charts/2.json/<student_id>')
def seed_chart_two(student_id):
    """ Passes data for days practiced over four weeks to chart #2 as JSON"""

    if 'student_id' in session:
        pass
    elif 'teacher_id' in session:
        teacher = crud.get_teacher_by_id(session['teacher_id'])
        valid_students = teacher.get_student_ids()

        if int(student_id or 0) in valid_students:
            crud.get_logs_by_student_id(int(student_id))
        else:
            return jsonify({'error': 'student not valid'})

    # x-axis data: dates in month (eventually divded into four weeks)
    dates_in_month = [] # holds todays date and previous 27 dates
    date = datetime.now()
    for _ in range(28):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        dates_in_month.append(dater)
        date = date - timedelta(days = 1) 

    log_date = []

    # y-axis data: days practiced in each week of the month
    for date in dates_in_month:
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, '%Y-%m-%d').date(), student_id) #finds and formatts all logged practice dates in DB
        if monthly_dates:
            log_date.append((date, 1)) #adds date and 1 to show a practice session occurred
        else:
            log_date.append((date, 0)) #adds date, 0 to signify no practice session that date

    data = {}
    data['dates_in_month'] = [datetime.strptime(date, '%Y-%m-%d').date().ctime()[4:10] for date, date_prac in log_date]
    data['log_date'] = [date_prac for date, date_prac in log_date]

    return jsonify(data)

@app.route('/charts/3.json/<student_id>')
def seed_chart_three(student_id):
    """ Passes data for minutes practiced over four weeks to chart #3 as JSON"""

    if 'student_id' in session:
        pass
    elif 'teacher_id' in session:
        teacher = crud.get_teacher_by_id(session['teacher_id'])
        valid_students = teacher.get_student_ids()

        if int(student_id or 0) in valid_students:
            crud.get_logs_by_student_id
        else:
            return jsonify({'error': 'student not valid'})


    # x-axis data: dates in month (eventually divded into four weeks)
    dates_in_month = [] # holds todays date and previous 27 dates as list items
    date = datetime.now()
    for _ in range(28):
        dater = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        dates_in_month.append(dater)
        date = date - timedelta(days=1)

    minutes_practiced = []

    # format_date = datetime.strptime(date, "%Y-%m-%d").date()

    # y-axis data: minutes practiced on each date in the month
    for date in dates_in_month:
        monthly_dates = crud.search_logs_by_date(datetime.strptime(date, '%Y-%m-%d').date(), student_id)
        if monthly_dates:
            minutes_practiced.append((date, monthly_dates.minutes_practiced))
        else:
            minutes_practiced.append((date, 0))

    data = {}
    data['dates_in_month'] = [datetime.strptime(date, '%Y-%m-%d').date().ctime()[4:10] for date, date_prac in minutes_practiced]
    #['2021-3-1', '2021-2-28', '2021-2-27', '2021-2-26', '2021-2-25', '2021-2-24', '2021-2-23', '2021-2-22', '2021-2-21', '2021-2-20', '2021-2-19', '2021-2-18', '2021-2-17', '2021-2-16', '2021-2-15', '2021-2-14', '2021-2-13', '2021-2-12', '2021-2-11', '2021-2-10', '2021-2-9', '2021-2-8', '2021-2-7', '2021-2-6', '2021-2-5', '2021-2-4', '2021-2-3', '2021-2-2']
    data['minutes_practiced'] = [min_prac for date, min_prac in minutes_practiced]
    # [('2021-3-1', 45), ('2021-2-28', 0), ('2021-2-27', 0), ('2021-2-26', 120), ('2021-2-25', 12), ('2021-2-24', 45), ('2021-2-23', 35), ('2021-2-22', 100), ('2021-2-21', 22), ('2021-2-20', 0), ('2021-2-19', 45), ('2021-2-18', 22), ('2021-2-17', 23), ('2021-2-16', 45), ('2021-2-15', 0), ('2021-2-14', 10), ('2021-2-13', 0), ('2021-2-12', 72), ('2021-2-11', 0), ('2021-2-10', 42), ('2021-2-9', 0), ('2021-2-8', 50), ('2021-2-7', 65), ('2021-2-6', 35), ('2021-2-5', 122), ('2021-2-4', 40), ('2021-2-3', 25), ('2021-2-2', 0)]


    return jsonify(data)

#_________________________________________functions for SMS messaging____________________________________________#
@app.route('/api/messages', methods=['POST'])
def send_message():
    """ Sends a text to a specific student from their teacher's profile page """

    # Get content from form
    student_id = request.form.get('phone_dropdown_id')
    text_message_content = request.form.get('message_content')
    student = crud.get_student_phone(student_id)
    student_num = student.student_phone

    # If testing, don't send the text
    if os.environ.get('TESTING'):
        return jsonify({'message_content': text_message_content})

    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    client.messages.create(
                    body=text_message_content,
                    to=str("1" + student_num),
                    from_=os.environ["TWILIO_PHONE"]
                )

    return jsonify({'message_content': text_message_content})

#_________________________________________________________________________________________________#

if __name__ == '__main__':
    # connect_to_db(app)
    app.run(host='0.0.0.0', port=5001, debug=True)
