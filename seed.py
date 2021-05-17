"""
This script will create new tables if your database is empty.

Use the scripts args/flags as follows:
    * `--dropdb` will drop all tables in database
    * `--createdb` will create all tables defined in `models.py` > in database
    * `--seed_data` will add data to database (from `seed_data.py`)

Example:
```bash
python seed.py --createdb --dropdb --seed_data
```
"""

import os
import sys
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

# ------------------------------------------------------------------------------
# Define args
import argparse


parser = argparse.ArgumentParser(description='Options for manipulating your db')
parser.add_argument('--dropdb', action='store_true', help='Do you want to drop the db?')
parser.add_argument('--createdb', action='store_true', help='Do you want to (re)create the db?')
parser.add_argument('--seed_data', action='store_true', help='Do you want to seed your db?')


args = parser.parse_args()


# ------------------------------------------------------------------------------

# The following commands are not ideal, since they execute as sudo
if args.dropdb:
    os.system('dropdb VMS')

if args.createdb:
    os.system('createdb VMS')

    # Connext to the db and create all the models defined
    model.connect_to_db(server.app)
    model.db.create_all()


# SKIP THE CRUD FUNCTIONALITY... USE `seed_data.py` instead
if args.seed_data:
    os.system('python seed_data.py')




# ------------------------------------------------------------------------------
