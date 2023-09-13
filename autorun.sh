#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell <<EOF
from django.contrib.auth.models import User
list_user = User.objects.all()
if (len(list_user)==0):
    User.objects.create_superuser("admin","","password")
EOF
python manage.py runserver 0.0.0.0:8000