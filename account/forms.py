"""
contains the forms for the account app
"""

from django.forms import ModelForm
from .models import User


class RegistrationForm(ModelForm):
	"""
	form for registering user
	"""
	class Meta:
		"""
		Meta Class for form containing details about the form
		"""
		model = User
		fields = ('first_name', 'last_name', 'password', 'email', 'username')
