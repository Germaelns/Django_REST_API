from django.urls import path
from .views import *

urlpatterns = [
    path('', user_post),
]
