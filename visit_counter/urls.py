from django.urls import path
from .api import count_visits

app_name = "visits"

urlpatterns = [path("api/visits", count_visits, name="visit_count")]
