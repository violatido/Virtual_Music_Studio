"""CRUD operations."""

from model import db, Teacher, Student, Log, connect_to_db

#______________________functions for creating table records___________________________#
def create_teacher(teacher_fname, 
                    teacher_lname, 
                    teacher_email, 
                    teacher_phone, 
                    teacher_password):
    """Creates a new teacher record"""

    teacher = Teacher(teacher_fname=teacher_fname, 
                        teacher_lname=teacher_lname, 
                        teacher_email=teacher_email,
                        teacher_phone=teacher_phone,
                        teacher_password=teacher_password
                        )

    db.session.add(teacher)
    db.session.commit()

    return teacher

def create_student(student_fname, 
                    student_lname, 
                    student_email, 
                    program_name, 
                    instrument, 
                    student_password,
                    teacher_obj):
    """Creates a new student record"""

    student = Student(student_fname=student_fname,
                        student_lname=student_lname,
                        student_email=student_email,
                        program_name=program_name, 
                        instrument=instrument,
                        student_password=student_password,
                        teacher=teacher_obj #using the teacher/student relationship
                        )

    db.session.add(student)
    db.session.commit()

    return student

def create_log(log_date, 
                student_id,
                minutes_practiced, 
                pieces_practiced, 
                practice_notes):
    """Creates a new practice log record"""
    
    log = Log(log_date=log_date, 
                student_id=student_id,
                minutes_practiced=minutes_practiced,
                pieces_practiced=pieces_practiced, 
                practice_notes=practice_notes
                )

    db.session.add(log)
    db.session.commit()

    return log 


#__________________________functions for User verification___________________________#
def verify_teacher(teacher_email, teacher_password):
    """Validates teacher email and password by finding matches in the database"""
    return Teacher.query.filter(Teacher.teacher_email == teacher_email, 
            Teacher.teacher_password == teacher_password).first()

def verify_student(student_email, student_password):
    """Validates student email and password by finding matches in the database"""
    return Student.query.filter(Student.student_email == student_email, 
            Student.student_password == student_password).first()

#__________________________functions for User verification___________________________#
def get_student_by_email(student_email): 
    """Finds all student info"""
    return Student.query.filter(Student.student_email == student_email).first()

def get_teacher_by_email(teacher_email): 
    """Finds all teacher info"""
    return Teacher.query.filter(Teacher.teacher_email == teacher_email).first()

def get_teacher_by_id(teacher_id):
    return Teacher.query.get(teacher_id)

def get_student_by_id(student_id):
    return Student.query.get(student_id)

def get_students_by_teacher_id(teacher_id):
    return Student.query.filter(Student.teacher_id == Teacher.teacher_id).first()

#__________________________functions for Finding Logs/Log info___________________________#

def get_logs_by_student_id(student_id):
    """ Finds all logs submitted by a specific student using their student ID """
    return Log.query.filter(Log.student_id == student_id).order_by(Log.log_date.desc()).all()

def get_minutes_practiced(student_id):
    """ Procures all minutes-practiced data per student """
    return Log.query.get(student_id)

def search_logs_by_date(log_date, student_id):
    return Log.query.filter(Log.log_date == log_date, Log.student_id == student_id).first()

#__________________________functions for Assigning Teachers___________________________#

def group_students_by_teacher(private_teacher):
    """ Locate all students by private teacher's name """
    return Student.query.filter(Student.private_teacher == private_teacher).all()

    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
