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
        return f'<User user_id={self.user_id} name={self.fname} {self.lname}>'


class Teacher(db.Model):
    """Data Model for Teacher IDs"""
    __tablename__ = 'teachers'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User', backref='teacher', uselist=False)

    def __repr__(self):
        """Show Teacher ID/Corresponding User Id"""
        return f'<Teacher teacher_id={self.teacher_id} name={self.user.fname} {self.user.lname}>'


class Student(db.Model):
    """Data Model for Student-specific Information"""
    __tablename__ = 'students'

    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    program_name = db.Column(db.String(50)) 
    instrument = db.Column(db.String(25), nullable=False)

    teacher = db.relationship('Teacher', backref='students')
    user = db.relationship('User', backref='student', uselist=False)


    def __repr__(self):
        """Show Student ID"""
        return f'<Student student_id={self.student_id} name={self.user.fname} {self.user.lname}>'


class Log(db.Model):
    """Data Model for Practice Logs"""
    __tablename__ = 'logs'
    
    log_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    log_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    pieces_practiced = db.Column(db.String(150), nullable=False)
    practice_notes = db.Column(db.String(200))

    student = db.relationship('Student', backref='logs')

    def __repr__(self):
        """Show Log Info"""
        return f'<Log log_date={self.log_date} student_id={self.student_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///VMS', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    # from server import app

    #sets Flask instance
    from flask import Flask
    app = Flask(__name__)

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.


    connect_to_db(app)
    db.create_all()

