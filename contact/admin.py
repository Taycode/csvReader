"""
Determines how the Admin should display models from Contact app
"""

from django.contrib import admin
from .models import Contact, Table


admin.site.register(Table)
