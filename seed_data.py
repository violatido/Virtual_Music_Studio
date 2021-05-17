"""
Populate database with records from serialized json format
"""

import os
import json
from datetime import datetime

from model import db, Teacher, Student, Log, Note, connect_to_db

import server

#import custom func
from utils.cipher import hash_input

# This essentially instantiates your app in order to connect to the db.
# That's not necessary – but we won't fix rn
connect_to_db(server.app)

db.create_all() # No need to create all, since the models already exist


# This session allows you to interact with your db
session = db.session





# ------------------------------------------------------------------------------
# CREATE TEACHERS


teacher_records = [

    dict(
        teacher_fname="Matthew",
        teacher_lname="Smith",
        teacher_email="msmith@gmail.com",
        teacher_phone="666-888-4444",
        teacher_password=hash_input("msmith"),
    ),

    dict(
        teacher_fname="Alice",
        teacher_lname="Baker",
        teacher_email="abaker@gmail.com",
        teacher_phone= "",
        teacher_password=hash_input("abaker"),
    )

]

for rec in teacher_records:


    # Check to see if your student exists, if so, skip
    if my_teacher := session.query(Teacher).filter_by(teacher_email=rec['teacher_email']).first():
        print(f'Teacher {my_teacher} already exists. Skipping')
        continue

    # Otherwise – create the teacher
    my_teacher = Teacher(**rec)

    # add them to the session
    session.add(my_teacher)

# commit the session
session.commit()




# ------------------------------------------------------------------------------
# CREATE STUDENTS

# Create a list of records for our student
student_records = [

    dict(
        student_fname="Olivia",
        student_lname="Rose",
        student_email="orose@gmail.com",
        program_name = "",
        instrument = "violin",
        student_password= hash_input("orose"),
        teacher_email = "abaker@gmail.com" # we'll use this query the teacher
    ),


    dict(
        student_fname="Alex",
        student_lname="Peters",
        student_email="apeters@gmail.com",
        program_name = "Klein High School",
        instrument = "viola",
        student_password= hash_input("apeters"),
        teacher_email = "msmith@gmail.com" # we'll use this query the teacher
    ),

    dict(
        student_fname="Sean",
        student_lname="Taylor",
        student_email="stay@aol.com",
        program_name = "Klein High School",
        instrument = "viola",
        student_password=hash_input("staylor"),
        teacher_email = "msmith@gmail.com" # we'll use this query the teacher
    )

]




for rec in student_records:


    # Check to see if your student exists, if so, skip
    if my_student := session.query(Student).filter_by(student_email=rec['student_email']).first():
        print(f'Student {my_student} already exists. Skipping')
        continue

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Get your teacher – and remove from the record
    teacher_email = rec.pop('teacher_email')
    my_teacher = session.query(Teacher).filter_by(teacher_email=teacher_email).first()


    # Instantiate your student
    my_student = Student(**rec)

    # Add your student to the session (get ready to be shunted to db)
    session.add(my_student)

    # Assign the student to the teacher
    # this will automatically assign the teacher id to the student
    my_student.teacher = my_teacher

    # Now what happens?
    # Try committing
    session.commit()

    # Use the following to determine if all the attributes were correctly set
    # print(my_student.__dict__)



# ------------------------------------------------------------------------------

# CREATE NOTES

note_records = [

    dict(
        student_email = "orose@gmail.com", # we'll use this to query the db
        note_created_at = datetime(year=2021, month=5, day=2, hour=15, minute=30), # eq. to `datetime(2021, 5, 2, 15, 30)`
        note_content="Came very prepared, but five minutes late"
    ),

    dict(
        student_email = "apeters@gmail.com", # we'll use this to query the db
        note_created_at = datetime(year=2021, month=3, day=5, hour=13, minute=30), # eq. to `datetime(2021, 5, 2, 15, 30)`
        note_content="Did not have his music"
    ),

    dict(
        student_email = "stay@aol.com", # we'll use this to query the db
        note_created_at = datetime(year=2021, month=3, day=1, hour=11, minute=30), # eq. to `datetime(2021, 5, 2, 15, 30)`
        note_content="Fantastic work"
    ),

    dict(
        student_email = "stay@aol.com", # we'll use this to query the db
        note_created_at = datetime(year=2021, month=3, day=8, hour=11, minute=30), # eq. to `datetime(2021, 5, 2, 15, 30)`
        note_content="Getting better at pacing."
    ),
]


# Will create duplicate notes, so you'll want to query notes first before creating

def note_already_exists(student_id, dt):
    """check to see if a student created a note at this time, u only need these 2 keys to match"""
    res = session.query(Note)\
        .filter(
            Note.student_id==student_id,
            Note.note_created_at==dt
        )\
        .count()

    return res > 0


# We don't need to query the teacher since every student has only 1 teacher
for rec in note_records:



    # Get yo student
    my_student = session.query(Student).filter_by(student_email=rec['student_email']).first()

     # make sure your student exists
    assert my_student


    # Check if note already exists:
    if note_already_exists(my_student.student_id, rec['note_created_at']):
        continue


    # Now create your note
    my_note = Note(
        teacher_id = my_student.teacher.teacher_id,
        student_id = my_student.student_id,
        note_created_at = rec['note_created_at'],
        note_content = rec['note_content']
    )
    session.add(my_note)


# Now commit (you only need to commit at the end.)
session.commit()


# ------------------------------------------------------------------------------
# CREATE LOGS


log_records = [

    dict(
        student_email = "apeters@gmail.com", # we'll use this to query the db
        log_date = datetime(year=2021, month=5, day=1), # will be set to midnight if no hour is specified
        minutes_practiced=15,
        pieces_practiced="Rebecca Clarke Morpheus",
        practice_notes="This piece is really hard!"
    ),

    dict(
        student_email = "apeters@gmail.com", # we'll use this to query the db
        log_date = datetime(year=2021, month=5, day=2), # will be set to midnight if no hour is specified
        minutes_practiced=35,
        pieces_practiced="Rebecca Clarke Morpheus",
        practice_notes="This piece is really hard!"
    ),

    dict(
        student_email = "apeters@gmail.com", # we'll use this to query the db
        log_date = datetime(year=2021, month=5, day=3), # will be set to midnight if no hour is specified
        minutes_practiced=122,
        pieces_practiced="Bach Suite 6 Allemande",
        practice_notes=None
    ),


    dict(
        student_email = "orose@gmail.com", # we'll use this to query the db
        log_date = datetime(year=2021, month=5, day=2), # will be set to midnight if no hour is specified
        minutes_practiced=35,
        pieces_practiced="Rebecca Clarke Morpheus",
        practice_notes="This piece is really hard!"
    ),

    dict(
        student_email = "orose@gmail.com", # we'll use this to query the db
        log_date = datetime(year=2021, month=5, day=5), # will be set to midnight if no hour is specified
        minutes_practiced=122,
        pieces_practiced="Bach Suite 6 Allemande",
        practice_notes=None
    ),

    dict(
        student_email = "orose@gmail.com", # we'll use this to query the db
        log_date = datetime(year=2021, month=5, day=9), # will be set to midnight if no hour is specified
        minutes_practiced=10,
        pieces_practiced="Bach Suite 6 Allemande",
        practice_notes="YOLO!"
    ),

]


def log_already_exists(student_id, dt):
    """check to see if a student created a note at this time, u only need these 2 keys to match"""
    res = session.query(Log)\
        .filter(
            Log.student_id==student_id,
            Log.log_date==dt
        )\
        .count()

    return res > 0


# Will create duplicate logs, so you'll want to query logs first before creating
for rec in log_records:


    # Get yo student
    my_student = session.query(Student).filter_by(student_email=rec['student_email']).first()

     # make sure your student exists
    assert my_student


    # Check if note already exists:
    if log_already_exists(my_student.student_id, rec['log_date']):
        continue




    my_log = Log(
        student_id = my_student.student_id,
        log_date = rec['log_date'],
        minutes_practiced = rec['minutes_practiced'],
        pieces_practiced = rec['pieces_practiced'],
        practice_notes = rec['practice_notes']
    )

    # Add to the session
    session.add(my_log)

# Finally, commit
session.commit()

#
