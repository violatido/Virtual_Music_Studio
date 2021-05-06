"""Revised script to selective seed the database."""

import os
import json
from datetime import datetime

from model import db, Teacher, Student, Log, Note, connect_to_db

import server

# This essentially instantiates your app in order to connect to the db.
# That's not necessary – but we won't fix rn
connect_to_db(server.app)
# model.db.create_all() # No need to create all, since the models already exist


# This session allows you to interact with your db
session = db.session




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
        student_password="orose",
        teacher_email = "abaker@gmail.com" # we'll use this query the teacher
    ),


    dict(
        student_fname="Alex",
        student_lname="Peters",
        student_email="apeters@gmail.com",
        program_name = "Klein High School",
        instrument = "viola",
        student_password="apeters",
        teacher_email = "msmith@gmail.com" # we'll use this query the teacher
    ),

    dict(
        student_fname="Sean",
        student_lname="Taylor",
        student_email="stay@aol.com",
        program_name = "Klein High School",
        instrument = "viola",
        student_password="staylor",
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
        note_student_name="Westin Humble",
        note_date="2/5/2021",
        note_time="3:30pm",
        note_content="Came very prepared, but five minutes late")

    )
]


# We don't need to query the teacher since every student has only 1 teacher


# note_1 = crud.create_note(teacher_id=3,
                # note_student_name="Westin Humble",
                # note_date="2/5/2021",
                # note_time="3:30pm",
                # note_content="Came very prepared, but five minutes late")

# note_2 = crud.create_note(teacher_id=3,
#                 note_student_name="Louis Jaffe",
#                 note_date="3/5/2021",
#                 note_time="1:30pm",
#                 note_content="Did not have his music")

# note_3 = crud.create_note(teacher_id=3,
#                 note_student_name="Franz Schubert",
#                 note_date="3/1/2021",
#                 note_time="11:30am",
#                 note_content="Fantastic work!")









# CREATE LOGS




#
