"""CRUD operations."""

# from model import db, User, Movie, Rating, connect_to_db
from model import db, User, Teacher, Student, Log, connect_to_db

# # Functions start here!
# """CRUD operations."""

def create_user(fname, lname, email, phone, password):
    """ Create an return a new user."""

    user = User(fname=fname, lname=lname, email=email, phone=phone, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_user_id(user_id):
    """ Get the user email using the primary key: user_id """
    return User.query.get(user_id)

def get_user_by_email(email):
    """ Get the user by using the email """
    return User.query.filter(User.email == email).first()


def create_teacher(user_id):
    """Create a teacher"""
    teacher = Teacher(user_id=user_id)

    db.session.add(teacher)
    db.session.commit()

    return teacher

def get_teacher_by_email(email):
    """Return teacher by email query"""
    return User.query.filter(User.email == email).first().teacher

#get user, exist? return teacher: nothing

def create_student(user_id, teacher_id,):
    """Create a student"""
    student = Student(user_id=user_id, teacher_id=teacher_id)

    db.session.add(student)
    db.session.commit()

    return student

def get_student_by_email(email):
    """Queries a student by email"""
    return User.query.filter(User.email == email).first().student



def create_log(student_id, log_date, start_time, end_time, pieces_practiced, practice_notes):
    """Creates a new practice log"""
    log = Log(student_id=student_id, log_date=log_date, start_time=start_time, end_time=end_time, pieces_practiced=pieces_practiced, practice_notes=practice_notes)

    db.session.add(log)
    db.session.commit()

    return log 

def get_log_student_email(email):
    """Queries a practice log"""
    return User.query.filter(User.email == email).first().student.logs


if __name__ == '__main__':
    from server import app
    connect_to_db(app)