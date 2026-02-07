import os
import django

os.environ.setdefault("DJANGO_SETTING_MODULE", "myproject1.settings")

django.setup()

from django.contrib.auth import get_user_model

User= get_user_model()

username = os.environ.get("DJANGO_SUPERUSERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Yes Superuser Created Successfully!!!")
else:
    print("No, Superuser already exists.")