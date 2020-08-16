"""
This describes the Schema of the database models related to the contact app
"""
from django.db import models
from account.models import User


class Contact(models.Model):
	"""
	This is the model for saving contacts a user has
	"""
	user = models.ForeignKey(User, models.CASCADE)
	name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	address = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.user.username + " - " + self.name


class Table(models.Model):
	"""
	This is the model for saving the names of the tables saved
	"""
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name
