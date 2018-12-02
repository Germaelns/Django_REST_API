# Create your tests here.
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.get('/posts/', {'title': 'remember to email dave'})
print(request.data)
