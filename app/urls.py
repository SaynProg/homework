from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePage, name='home'),
	path('countries-list', views.CountriesListPage, name='countries-list'),
	path('countries-list/<int:pk>', views.CountryPage, name='country'),
	path('languages', views.LanguagesPage, name='languages'),
]