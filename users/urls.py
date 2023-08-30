from django.urls import path
from .api import rest_api
from .views import home

app_name = 'users'

urlpatterns = [
    path("", home, name="home"),
    path("api/users/", rest_api, name="list_users")
]
