""" Define Model Classes """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()


class Teacher(db.Model):
    """Data Model for Teacher IDs"""
    __tablename__ = 'teachers'
    
    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    teacher_fname = db.Column(db.String(25), nullable=False)
    teacher_lname = db.Column(db.String(25), nullable=False)
    teacher_email = db.Column(db.String(50), nullable=False)
    teacher_phone = db.Column(db.String(25))
    teacher_password = db.Column(db.String(50), nullable=False)

    # kathy: establish student/teacher relationship in the teacher table
    students = db.relationship('Student')

    def __repr__(self):
        """Show Teacher ID/Corresponding User Id"""
        return f'<Teacher teacher_id={self.teacher_id} teacher_name={self.teacher_fname} {self.teacher_lname}>'

############################################################################

class Student(db.Model):
    """Data Model for Student-specific Information"""
    __tablename__ = 'students'
    
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'))
    student_fname = db.Column(db.String(25), nullable=False)
    student_lname = db.Column(db.String(25), nullable=False)
    student_email = db.Column(db.String(50), nullable=False)
    student_password = db.Column(db.String(50), nullable=False)
    program_name = db.Column(db.String(50)) 
    instrument = db.Column(db.String(25), nullable=False)

    # kathy: don't put the teacher/student relationship in the student table
    teacher = db.relationship('Teacher')
    # # kathy: put student/log relationship in the student table 
    logs = db.relationship('Log', backref='student', uselist=False)

    def __repr__(self):
        """Show Student ID"""
        return f'<Student student_id={self.student_id} student_name = {self.student_fname} {self.student_lname}>'

########################################################################

class Log(db.Model):
    """Data Model for Practice Logs"""
    __tablename__ = 'logs'
    
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    log_date = db.Column(db.Date, nullable=False)
    minutes_practiced = db.Column(db.Integer, nullable=False)
    pieces_practiced = db.Column(db.String(150), nullable=False)
    practice_notes = db.Column(db.String(200))

    # kathy: don't put student/log relationship in the log table
    # student_id=db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)

    def __repr__(self):
        """Show Log Info"""
        return f'<Log log_date={self.log_date} student_id={self.student_id} log_id={self.log_id}'
        # using student table attributes in the repr return statement:
        # return f'<Log log_date={self.log_date} student_name={self.student.fname} {self.student.lname}>'

############################################################################

def connect_to_db(flask_app, db_uri='postgresql:///VMS', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    db.create_all()
