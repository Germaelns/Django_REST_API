import json

import requests
from django.test import TestCase
from rest_framework import status

from .views import PostApiView


class PostsTest(TestCase):

    def create_post(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "email": "your email",
            "first_name": "your name",
            "last_name": "your surname",
            "password": "your password"
        }

        headers = {
            "Content-Type": "application/json"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(PostApiView(request), status.HTTP_201_CREATED)

    def get_post(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "email": "your email",
            "first_name": "your name",
            "last_name": "your surname",
            "password": "your password"
        }

        headers = {
            "Content-Type": "application/json"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(PostApiView(request), status.HTTP_201_CREATED)