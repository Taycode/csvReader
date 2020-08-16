"""
Describes the View of the contact app
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine, Table as sqlTable, MetaData
from sqlalchemy.orm import sessionmaker
from .models import Table
import json

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = 'postgresql://{user}:{password}@db:5432/{database_name}'.format(
	user=user,
	password=password,
	database_name=database_name,
)

engine = create_engine(database_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
meta = MetaData(engine)
connection = engine.connect()


class HomePage(View):
	"""
	Describes the Home page of the contact app
	"""

	@staticmethod
	def get(request):
		"""

		:param request:
		:return:
		"""
		tables = Table.objects.all()
		return render(request, 'contact/homepage.html', {'tables': tables})

	@staticmethod
	def post(request):
		"""

		:param request:
		:return:
		"""
		table_name = request.POST.get('tableName')
		Table(name=table_name).save()
		file = request.FILES['csv_file']
		data = pd.read_csv(file)
		data.to_sql(table_name, con=engine)
		return redirect('contact:home')


class ViewTableData(View):
	"""
	This is for viewing the data in a table
	"""

	@staticmethod
	def get(request, pk):
		"""
		This is used to get the data in a table
		:param request:
		:param pk:
		:return:
		"""
		table_model = Table.objects.get(id=pk)
		sale_table = sqlTable(table_model.name, meta, autoload=True)
		select_statement = sale_table.select()
		result = connection.execute(select_statement)
		to_be_sent_result = [dict(_) for _ in list(result)]
		# return HttpResponse(json.dumps(to_be_sent_result), content_type='application/json')
		return JsonResponse(to_be_sent_result, safe=False)


class RenderTableData(View):
	"""
	This is for Rendering the Table Data
	"""

	@staticmethod
	def get(request, pk):
		"""

		:param request:
		:param pk:
		:return:
		"""

		return render(request, 'contact/data.html', {'pk': pk})
