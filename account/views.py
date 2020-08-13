"""
This contains the Views of the app
"""

from django.shortcuts import render
from django.views import View
from .models import User
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout


class RegisterView(View):
	"""
	This view is used to register users
	"""
	@staticmethod
	def get(request):
		"""
		Returns template for registration

		:param request:
		:return:
		"""
		return render(request, 'account/register.html')

	@staticmethod
	def post(request):

		"""
		processes Registration of user
		:param request:
		:return:
		"""

		form = RegistrationForm(request.POST)

		if form.is_valid():
			password = request.POST.get('password')
			saved = form.save(commit=False)
			saved.set_password(password)
			saved.save()
			return render(request, 'account/homepage.html')
		else:
			print(form.errors)
			return render(request, 'account/register.html', {"form": form})


class LoginView(View):
	"""
	This View is for authenticating users
	"""

	@staticmethod
	def get(request):
		"""
		This returns the Login template
		:param request:
		:return:
		"""
		logout(request)
		return render(request, 'account/login.html')

	@staticmethod
	def post(request):
		"""
		This processes Login for the app
		:param request:
		:return:
		"""
		logout(request)
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return render(request, 'account/homepage.html')

		return render(request, 'account/login.html', {
			"message": "Credentials are incorrect",
			"username": username, "password": password
		})
