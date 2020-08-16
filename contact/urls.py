"""
This describes the URL routing of the Contact APP
"""

from django.urls import path
from .views import HomePage, ViewTableData, RenderTableData


urlpatterns = [
	path('', HomePage.as_view(), name='home'),
	path('<int:pk>/', ViewTableData.as_view()),
	path('view/<int:pk>/', RenderTableData.as_view(), name='view_data')
]
