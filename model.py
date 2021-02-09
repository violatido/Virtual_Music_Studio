""" Define Model Classes """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Data model for all users """
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(9))
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """ Show User Id and names """
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname}>'


class Teacher(db.Model):
    """ Data Model for Teacher IDs """
    __tablename__ = 'teachers'

    teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integers, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        """ Show Teacher ID/Corresponding User Id """
        return f'<Teacher teacher={self.teacher} user_id={self.user_id}>'


class Student(db.Model):