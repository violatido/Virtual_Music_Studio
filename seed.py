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

m_s = crud.create_teacher(teacher_fname="Matthew",
                            teacher_lname="Smith",
                            teacher_email="msmith@gmail.com",
                            teacher_phone="666-888-4444",
                            teacher_password="!!password1!!",
                        )

a_b = crud.create_teacher(teacher_fname="Alice",
                            teacher_lname="Baker",
                            teacher_email="abakes@gmail.com",
                            teacher_phone= "",
                            teacher_password="??password2??",
                        )

o_r = crud.create_student(student_fname="Olivia",
                            student_lname="Rose",
                            student_email="orose@gmail.com",
                            private_teacher="323-145-1288",
                            program_name = "",
                            instrument = "viola",
                            student_password="##student_password3##",
                        )

a_p = crud.create_student(student_fname="Alex",
                            student_lname="Peterson",
                            student_email="apete@yahoo.com",
                            private_teacher="939-717-2288",
                            program_name = "",
                            instrument = "viola",
                            student_password="$$pasword4$$",
                        )

m_s = crud.create_student(student_fname="Sean",
                            student_lname="Taylor",
                            student_email="stay@aol.com",
                            private_teacher="",
                            program_name = "",
                            instrument = "viola",
                            student_password="Schubert Arpeggione Sonata",
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


