from django.db import models

class Language(models.Model):
	name = models.CharField('Язык', max_length=1000)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Язык"
		verbose_name_plural = "Языки"

class Country(models.Model):
	name = models.CharField('Название страны', max_length=1000)
	languages = models.ManyToManyField(Language)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Страна"
		verbose_name_plural = "Страны"