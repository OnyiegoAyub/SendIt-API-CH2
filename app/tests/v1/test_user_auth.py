
import unittest
import json
from app import create_app


class TestUserCase(unittest.TestCase):

  def setUp(self):

    create_app().testing = True #???
    '''create an instance of a flask application just as you would create  a flask app,
       but in this case you pass to it a test client which means you are running a test instance'''
    self.app = create_app().test_client() #???
    self.data = {
        "user_id": 1,
        "username": "Ayub",
        "role": "Admin",
        "email": "ayub@gmail.com",
        "password": "ayub"

    }

  def test_create_user(self):
    response = self.app.post('/api/v1/users', data=json.dumps(self.data), content_type='application/json')
    self.assertEqual(response.status_code, 201)

  def test_get_all_users(self):
    response = self.app.get('api/v1/users')
    self.assertEqual(response.status_code, 200)

  def test_get_single_user(self):
    response = self.app.get('api/v1/users/1')
    self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
  unittest.main()
