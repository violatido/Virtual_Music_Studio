""" Define Model Classes For Virtual Music Studio App """
import deprecation

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

# sqlalchemy specific
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy




db = SQLAlchemy()


class Teacher(db.Model):
    """Data Model for Teacher userse"""
    __tablename__ = 'teachers'

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    teacher_fname = db.Column(db.String(25), nullable=False)
    teacher_lname = db.Column(db.String(25), nullable=False)
    teacher_email = db.Column(db.String(50), nullable=False, unique=True)
    teacher_phone = db.Column(db.String(25))
    teacher_password = db.Column(db.String(50), nullable=False)

    students = db.relationship('Student')
    student_ids = association_proxy('students', 'student_id',
        info='Use this to get all student ids from a teacher\'s students')

    notes = db.relationship('Note', backref='teacher', order_by='Note.note_id')


    @hybrid_property
    def full_name(self):
        """Make full name as a hybrid attribute"""
        tmp = (self.teacher_fname, self.teacher_lname)
        tmp_filtered = filter(None, tmp)

        return ' '.join(tmp_filtered)



    def __repr__(self):
        """Show Teacher ID and full name"""
        return f'<Teacher teacher_id={self.teacher_id} teacher_name={self.full_name}>'


    # utilize abstraction in the teacher class to allow teachers to view student info
    @deprecation.deprecated(details="Use the association proxy `teacher.student_ids` instead")
    def get_student_ids(self):
        """ Gives teacher access to their students's student IDs """
        if self.students:
            student_ids_lst = [student.student_id for student in self.students]
            return set(student_ids_lst)
        else:
            return set()

#################################################################################################################

class Student(db.Model):
    """Data Model for Student users"""
    __tablename__ = 'students'

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'))
    student_fname = db.Column(db.String(25), nullable=False)
    student_lname = db.Column(db.String(25), nullable=False)
    student_email = db.Column(db.String(50), nullable=False, unique=True)
    student_password = db.Column(db.String(50), nullable=False)
    program_name = db.Column(db.String(50))
    instrument = db.Column(db.String(25), nullable=False)
    student_phone = db.Column(db.String(25))

    teacher = db.relationship('Teacher')
    logs = db.relationship('Log', backref='student', order_by='Log.log_date.desc()')
    notes = db.relationship('Note', backref='student', order_by='Note.note_created_at.desc()')

    @hybrid_property
    def full_name(self):
        """Make full name as a hybrid attribute"""
        tmp = (self.student_fname, self.student_lname)
        tmp_filtered = map(str, filter(None, tmp))

        return ' '.join(tmp_filtered)


    def __repr__(self):
        """Show Student ID and full name"""
        return f'<Student student_id={self.student_id} student_name = {self.full_name}>'

#################################################################################################################

class Log(db.Model):
    """Data Model for Practice Logs"""
    __tablename__ = 'logs'

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    log_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    minutes_practiced = db.Column(db.SmallInteger, nullable=False)
    pieces_practiced = db.Column(db.String(150), nullable=False)
    practice_notes = db.Column(db.String(200))

    def __repr__(self):
        """Show Log date, ID, and ID of student who created the log"""
        return f'<Log log_date={self.log_date} student_id={self.student_id} log_id={self.log_id}'

#################################################################################################################

class Note(db.Model):
    """Data Model for Teacher Lesson Notes"""

    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False, comment='Added by Yaakov')

    note_content = db.Column(db.String, nullable=False)
    note_created_at = db.Column(db.DateTime, nullable=False, comment='YB: store date and time in one column...')



    def __repr__(self):
        """Show Teacher Note ID and date"""
        return f'<note teacher_id={self.teacher_id} student_id={self.student_id} note_id={self.note_id} note_date = {self.note_created_at}>'

#################################################################################################################


def connect_to_db(flask_app, echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5433/postgres'
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    db.create_all()
