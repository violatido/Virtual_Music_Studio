import unittest

from server import app
from model import db

TEST_DB = 'postgresql:///VMS'


# Reference: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB
        app.config['SQLALCHEMY_ECHO'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.app = app
        db.init_app(app)

        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

# create student to login as in the test, rather than seed.py data

    ###############
    #### tests ####
    ###############

    def test_student_login(self):
        response = self.app.post('/student-portal', data=dict(
            student_login_email = 'orose@gmail.com',
            student_login_pw = 'orose'
        ), follow_redirects = True)
        assert response.status_code == 200
        assert b'Welcome, Olivia Rose' in response.data

# returns 200 response:
# moves to next page, forwards to student page (why assert b sys "Welcome")

    def test_student_cannot_login_with_incorrect_password(self):
        response = self.app.post('/student-portal', data=dict(
            student_login_email = 'orose@gmail.com',
            student_login_pw = 'bad_password'
        ), follow_redirects = True)
        assert response.status_code == 200 # this should be a 401
        assert b'{"login credentials incorrect"}' in response.data

# this is negative test for bad password
# 401 = unauthorized 

if __name__ == "__main__":
    unittest.main()