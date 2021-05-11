"""
CRUD operations.

.. todo:
    * We may chose to remove this submodule and replace with more transparent methods
"""
import deprecation
from model import db, Teacher, Student, Log, Note, connect_to_db
from sqlalchemy import func

#______________________functions for creating table records___________________________#
def create_teacher(teacher_fname,
                    teacher_lname,
                    teacher_email,
                    teacher_phone,
                    teacher_password):
    """Creates a new teacher record"""

    if not teacher_email:
        raise ValueError(f'{teacher_email=}')

    # Check if email is already in use:
    if teacher := db.session.query(Teacher).filter_by(teacher_email=teacher_email).first():
        # Either return False which will cause an error – or return the teacher – in which
        # case, your method should be renamed `get_or_create_teacher()`
        return False

    teacher = Teacher(teacher_fname=teacher_fname,
                        teacher_lname=teacher_lname,
                        teacher_email=teacher_email,
                        teacher_phone=teacher_phone,
                        teacher_password=teacher_password
                        )

    db.session.add(teacher)
    db.session.commit()

    # refresh to get the teacher with all their data
    db.session.refresh(teacher)

    return teacher

def create_student(student_fname,
                    student_lname,
                    student_email,
                    program_name,
                    instrument,
                    student_password,
                    student_phone,
                    teacher_id):
    """Creates a new student record"""

    student = Student(student_fname=student_fname,
                        student_lname=student_lname,
                        student_email=student_email,
                        program_name=program_name,
                        instrument=instrument,
                        student_password=student_password,
                        student_phone=student_phone,
                        teacher_id=teacher_id # easier to pass primary keys than entire objects
                        )

    db.session.add(student)
    db.session.commit()

    # If you have issues with the student's data, consider refreshing the student object
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

def create_note(teacher_id,
                student_id,
                note_created_at,
                note_content):

    """Creates a new teacher note record"""

    # Allows querying of student by full name – Hopefull this works!
    # Querying by hybrid attribute doesn't seem to be working unfortunately
    # student_id = db.session.query(Student.student_id)\
    #     .filter(
    #         func.concat(
    #             Student.student_fname,
    #             ' ',
    #             Student.student_lname
    #         ) == note_student_name
    #     ).first()

    # Only allow if student id exists
    # if not student_id:
    #     return None

    note = Note(teacher_id=teacher_id,
                student_id=student_id,
                note_created_at=note_created_at,
                note_content=note_content
                )


    db.session.add(note)
    db.session.commit()

    return note

#__________________________functions for User verification___________________________#
def verify_teacher(teacher_email, teacher_password):
    """Validates teacher email and password by finding matches in the database"""

    return Teacher.query.filter(Teacher.teacher_email == teacher_email,
            Teacher.teacher_password == teacher_password).first()

def verify_student(student_email, student_password):
    """Validates student email and password by finding matches in the database"""

    return Student.query.filter(Student.student_email == student_email,
            Student.student_password == student_password).first()

def check_email(teacher_email):
    """Return database row that matches given email."""

    return User.query.filter(Teacher.teacher_email == teacher_email).first()
#__________________________functions for User verification___________________________#
def get_student_by_email(student_email):
    """Finds all student info"""

    return Student.query.filter(Student.student_email == student_email).first()

def get_teacher_by_email(teacher_email):
    """Finds all teacher info"""

    return Teacher.query.filter(Teacher.teacher_email == teacher_email).first()

def get_teacher_by_id(teacher_id):
    """Finds all teacher info by teacher ID"""

    return Teacher.query.get(teacher_id)

def get_student_by_id(student_id):
    """Finds all student info by student ID"""

    return Student.query.get(student_id)

def get_students_by_teacher_id(teacher_id):
    """Finds all students who belong to a particular teacher's studio"""

    return Student.query.filter(Student.teacher_id == teacher_id).order_by(Student.student_id.desc()).all()

#__________________________functions for Notes/Logs___________________________#

@deprecation.deprecated(details="Use the relationship `teacher.notes` instead")
def get_notes_by_teacher_id(teacher_id):
    """ Finds all notes submitted by a specific teacher using their teacher ID """

    return Note.query.filter(Note.teacher_id == teacher_id).order_by(Note.note_id).all()


@deprecation.deprecated(details="Use the relationship `child.logs` instead")
def get_logs_by_student_id(student_id):
    """
    Finds all logs submitted by a specific student using their student ID
    """
    return Log.query.filter(Log.student_id == student_id).order_by(Log.log_date.desc()).all()


def get_minutes_practiced(student_id):
    """ Procures all minutes-practiced data per student """

    return Log.query.get(student_id)

def search_logs_by_date(log_date, student_id):
    """Finds all kigs written by a student on a particular date"""

    return Log.query.filter(Log.log_date == log_date, Log.student_id == student_id).first()

#__________________________functions for Assigning Teachers___________________________#

def group_students_by_teacher(private_teacher, student_id):
    """ Locates all students by their private teacher's name """

    return Student.query.filter(Student.private_teacher == private_teacher).order_by(Student.student_id.desc()).all()

def get_student_phone(student_id):
    """Pulls the phone number of a specific student for text messaging"""

    return Student.query.filter(Student.student_id == student_id).first()

def get_full_student_name(student_id):
    """Grabs first and last name of a student using their student ID number"""

    student = Student.query.filter(Student.student_id == student_id).first()
    student_full_name = student.student_fname + ' ' + student.student_lname

    return student_full_name












# ------------------------------------------------------------------------------


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
