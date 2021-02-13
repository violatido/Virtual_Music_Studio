"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb VMS')
os.system('createdb VMS')
model.connect_to_db(server.app)
model.db.create_all()

m_s = crud.create_user(fname="Matthew",
                            lname="Smith",
                            email="msmith@gmail.com",
                            phone="666-888-4444",
                            password="!!password1!!",
                        )

a_b = crud.create_user(fname="Alice",
                            lname="Baker",
                            email="abakes@gmail.com",
                            phone= "",
                            password="??password2??",
                        )

o_r = crud.create_user(fname="Olivia",
                            lname="Rose",
                            email="orose@gmail.com",
                            phone="323-145-1288",
                            password="##password3##",
                        )

a_p = crud.create_user(fname="Alex",
                            lname="Peterson",
                            email="apete@yahoo.com",
                            phone="939-717-2288",
                            password="$$pasword4$$",
                        )

m_s = crud.create_user(fname="Sean",
                            lname="Taylor",
                            email="stay@aol.com",
                            phone="",
                            password="Schubert Arpeggione Sonata",
                        )

log_a = crud.create_log(student_id=1,
                            log_date="1/2/2021",
                            start_time="4:50pm",
                            end_time="5:30pm",
                            pieces_practiced="Rebecca Clarke Morpheus",
                            practice_notes="This piece is really hard!"
                        )

log_b = crud.create_log(student_id=1,
                            log_date="2/5/2021",
                            start_time="2:05pm",
                            end_time="2:45pm",
                            pieces_practiced="Bach Suite 6 Allemande",
                            practice_notes=""
                        )

log_c = crud.create_log(student_id=2,
                            log_date="2/15/2021",
                            start_time="11:00am",
                            end_time="12:30pm",
                            pieces_practiced="Walton Viola Concerto",
                            practice_notes="Are you trying to kill me?"
                        )                                                                                        





# def seed_users(filename):
#     teachers_in_db = []
#     students_in_db = []

#     f = open(filename, 'r')

#     for entry in f:
#         entry = entry.rstrip().split('|')

#         if entry[0] == "Student": #crud.create_student (crud.py function takes in an object)
#             students_in_db.append(entry[1])
#         else:
#             teachers_in_db.append(entry[1])

#         # crud.create_user()
    
#     return students_in_db



# def seed_logs(filename):
#     logs_in_db = []

#     f = open(filename, 'r')

#     for entry in f:
#         entry = entry.rstrip().split('|')
#         logs_in_db.append(entry)
    
#     return logs_in_db

