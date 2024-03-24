from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

def get_username(self):
    return self.username

User.add_to_class("__str__", get_username)