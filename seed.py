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
                            teacher_password="msmith",
                        )

a_b = crud.create_teacher(teacher_fname="Alice",
                            teacher_lname="Baker",
                            teacher_email="abaker@gmail.com",
                            teacher_phone= "",
                            teacher_password="abaker",
                        )

o_r = crud.create_student(student_fname="Olivia",
                            student_lname="Rose",
                            student_email="orose@gmail.com",
                            program_name = "",
                            instrument = "violin",
                            student_password="orose",
                            teacher_obj=a_b
                        )

# a_p = crud.create_student(student_fname="Alex",
#                             student_lname="Peters",
#                             student_email="apeters@gmail.com",
#                             program_name = "Klein High School",
#                             instrument = "viola",
#                             student_password="apeters",
#                         )

# m_s = crud.create_student(student_fname="Sean",
#                             student_lname="Taylor",
#                             student_email="stay@aol.com",
#                             program_name = "Klein High School",
#                             instrument = "viola",
#                             student_password="staylor",
#                         )

log_a = crud.create_log(student_id=1,
                            log_date="1/2/2021",
                            minutes_practiced=35,
                            pieces_practiced="Rebecca Clarke Morpheus",
                            practice_notes="This piece is really hard!"
                        )

log_b = crud.create_log(student_id=1,
                            log_date="2/5/2021",
                            minutes_practiced=122,
                            pieces_practiced="Bach Suite 6 Allemande",
                            practice_notes=""
                        )

# log_c = crud.create_log(student_id=2,
#                             log_date="2/15/2021",
#                             minutes_practiced=13,
#                             pieces_practiced="Walton Viola Concerto",
#                             practice_notes="Are you trying to kill me?"
#                         )              


