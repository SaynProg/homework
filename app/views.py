from django.shortcuts import render
from .models import *

def HomePage(request):
	return render(request, 'home.html')

def CountriesListPage(request):
	items = Country.objects.all()
	return render(request, 'country_list.html', {'items':items})

def CountryPage(request, pk):
	item = Country.objects.get(id = pk)
	langs = item.languages.all
	return render(request, 'country.html', {'item':item, 'langs':langs})

def LanguagesPage(request):
	items = Language.objects.all()
	return render(request, 'languages.html', {'items':items})