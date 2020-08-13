"""
This describes the schema of the data in the database
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	"""
	Custom User Model
	"""
	email = models.EmailField(unique=True)
