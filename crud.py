"""CRUD operations."""

# from model import db, User, Movie, Rating, connect_to_db
from model import db, User, Teacher, Student, Log, connect_to_db

# # Functions start here!
# """CRUD operations."""

def create_user(email, password, fname, lname):
    """ Create an return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname)

    db.session.add(user)
    db.session.commt()

    return user

def get_user_by_id(user_id):
    """ Get the user email using the primary key: user_id """
    return User.query.get(user_id)

def get_user_by_email(email):
    """ Get the user by using the email """
    return User.query.filter(User.email == email).first()





if __name__ == '__main__':
    from server import app
    connect_to_db(app)