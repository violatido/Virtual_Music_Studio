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

# log_a = crud.create_log(student_id=1,
#                             log_date="1/2/2021",
#                             minutes_practiced=35,
#                             pieces_practiced="Rebecca Clarke Morpheus",
#                             practice_notes="This piece is really hard!"
#                         )

# log_b = crud.create_log(student_id=1,
#                             log_date="2/5/2021",
#                             minutes_practiced=122,
#                             pieces_practiced="Bach Suite 6 Allemande",
#                             practice_notes=""
#                         )

# log_c = crud.create_log(student_id=2,
#                             log_date="2/15/2021",
#                             minutes_practiced=13,
#                             pieces_practiced="Walton Viola Concerto",
#                             practice_notes="Are you trying to kill me?"
#                         )              

# log_d = crud.create_log(student_id=6,
#                             log_date="03/01/2021",
#                             minutes_practiced=5,
#                             pieces_practiced="Piano Sonata No 1",
#                             practice_notes=""
#                         )  

# log_e = crud.create_log(student_id=6,
#                             log_date="03/02/2021",
#                             minutes_practiced=82,
#                             pieces_practiced="Piano Sonata No 1",
#                             practice_notes=""
#                         )  

# log_f = crud.create_log(student_id=6,
#                             log_date="03/05/2021",
#                             minutes_practiced=45,
#                             pieces_practiced="Piano Sonata No 1",
#                             practice_notes=""
#                         )  

# log_g = crud.create_log(student_id=6,
#                             log_date="02/28/2021",
#                             minutes_practiced=73,
#                             pieces_practiced="Piano Sonata No 1",
#                             practice_notes=""
#                         )  

# log_h = crud.create_log(student_id=5,
#                             log_date="02/28/2021",
#                             minutes_practiced=135,
#                             pieces_practiced="Elegy",
#                             practice_notes=""
#                         )  

# log_i = crud.create_log(student_id=5,
#                             log_date="02/03/2021",
#                             minutes_practiced=35,
#                             pieces_practiced="Elegy",
#                             practice_notes=""
#                         )  

# log_j = crud.create_log(student_id=5,
#                             log_date="03/04/2021",
#                             minutes_practiced=35,
#                             pieces_practiced="Elegy",
#                             practice_notes=""
#                         )  

# log_k = crud.create_log(student_id=5,
#                             log_date="03/01/2021",
#                             minutes_practiced=56,
#                             pieces_practiced="Piano Sonata No 1",
#                             practice_notes="Morpheus"
#                         )  

# log_l = crud.create_log(student_id=5,
#                             log_date="02/28/2021",
#                             minutes_practiced=35,
#                             pieces_practiced="Morpheus and Scales",
#                             practice_notes=""
#                         )  

# log_m = crud.create_log(student_id=5,
#                             log_date="02/28/2021",
#                             minutes_practiced=35,
#                             pieces_practiced="Morpheus and Scales",
#                             practice_notes=""
#                         )  


# log_n = crud.create_log(student_id=5,
#                             log_date="02/28/2021",
#                             minutes_practiced=135,
#                             pieces_practiced="Morpheus and Scales",
#                             practice_notes=""
#                         )  


# log_o = crud.create_log(student_id=5,
#                             log_date="03/05/2021",
#                             minutes_practiced=120,
#                             pieces_practiced="Elegy",
#                             practice_notes=""
#                         )  


# log_p = crud.create_log(student_id=5,
#                             log_date="02/28/2021",
#                             minutes_practiced=35,
#                             pieces_practiced="Morpheus and Scales",
#                             practice_notes=""
#                         )  


# log_q = crud.create_log(student_id=5,
#                             log_date="02/16/2021",
#                             minutes_practiced=14,
#                             pieces_practiced="Scales",
#                             practice_notes=""
#                         )  
# ADD COLUMN new_column_name data_type constraint