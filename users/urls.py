from django.urls import path
from .api import list_users
from .views import home

app_name = "users"

urlpatterns = [
    path("", home, name="home"),
    path("api/users/", list_users, name="list_users"),
]
