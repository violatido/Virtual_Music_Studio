"""CRUD operations."""

from model import db, Teacher, Student, Log, connect_to_db

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
                    private_teacher, 
                    program_name, 
                    instrument, 
                    student_password):
    """Creates a new student record"""

    student = Student(student_fname=student_fname,
                        student_lname=student_lname,
                        student_email=student_email,
                        private_teacher=private_teacher,
                        program_name=program_name, 
                        instrument=instrument,
                        student_password=student_password
                        )

    db.session.add(student)
    db.session.commit()

    return student


def create_log(log_date, 
                start_time, 
                end_time, 
                pieces_practiced, 
                practice_notes):
    """Creates a new practice log record"""
    
    log = Log(log_date=log_date, 
                start_time=start_time, 
                end_time=end_time, 
                pieces_practiced=pieces_practiced, 
                practice_notes=practice_notes
                )

    db.session.add(log)
    db.session.commit()

    return log 

def verify_teacher(teacher_email, teacher_password):
    if teacher_email != None:
        return "hello"




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
