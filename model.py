""" Define Model Classes """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for all users"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(9))
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Show User Id and names"""
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname}>'


class Teacher(db.Model):
    """Data Model for Teacher IDs"""
    __tablename__ = 'teachers'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        """Show Teacher ID/Corresponding User Id"""
        return f'<Teacher teacher_id={self.teacher_id} user_id={self.user_id}>'


class Student(db.Model):
    """Data Model for Student-specific Information"""
    __tablename__ = 'students'

    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    program_name = db.Columnt(db.String(50), nullable=True)

    def __repr__(self):
        """Show Student ID"""
        return f'<Student student_id={self.student_id} user_id={self.user_id}>'


class Log(db.Model):
    """Data Model for Practice Logs"""
    __tablename__ = 'logs'

    
    log_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    log_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Timestamp, nullable=False)
    end_time = db.Column(db.Timestamp, nullable=False)
    pieces_practiced = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        """Show Log Info"""
        return f'<Log log_date={self.log_date} student_id={self.student_id}>'
