from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def HomePage(request):
	return render(request, 'home.html')

def CountriesListPage(request):
	items = Country.objects.all()
	paginator = Paginator(items, 10)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)
	return render(request, 'country_list.html', {'items':page_obj})

def CountryPage(request, pk):
	item = Country.objects.get(id = pk)
	langs = item.languages.all
	return render(request, 'country.html', {'item':item, 'langs':langs})

def LanguagesPage(request):
	items = Language.objects.all()
	return render(request, 'languages.html', {'items':items})