import json

import requests
from django.test import TestCase
from rest_framework import status

from .views import CreateUserAPIView


class UserTest(TestCase):

    def test_good_post_request(self):
        url = 'http://127.0.0.1:8000/users/'

        payload = {
            "email": "nsheva@gmail.com",
            "first_name": "Nikolay",
            "last_name": "Shevchenko",
            "password": "sheva"
        }

        headers = {
            "Content-Type": "application/json"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(CreateUserAPIView(request), status.HTTP_201_CREATED)
