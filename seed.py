"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

# import crud
import model
# import server


# os.system('dropdb VMS')
# os.system('createdb VMS')
# model.connect_to_db(server.app)
# model.db.create_all()



def seed_data(filename):
    teachers_in_db = []
    students_in_db = []

    f = open(filename, 'r')

    for entry in f:

        # position, first, last, email, phone, password, program  = entry.rstrip().split('|')
        entry = entry.rstrip().split('|')

        if entry[0] == "Student": #crud.create_student (crud.py function takes in an object)
            students_in_db.append(entry[1])
        else:
            teachers_in_db.append(entry[1])
    
    return students_in_db

print(seed_data("data.txt"))

# data.txt seed_student_teacher = take user information and put in student or teacher lists
# log.txt seed_logs 
# lsits unnecessay. once sent to crud, will be in database 