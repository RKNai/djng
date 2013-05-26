from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Realplace(models.Model):

	userplace = models.CharField(max_length=80)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("Realplacespage")

class Place(models.Model):

	name = models.CharField(max_length=80)
	description = models.CharField(max_length=1000)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("PlacesPage")


class Castle(models.Model):
	name = models.CharField(max_length=80)
	place = models.ForeignKey(Place)
	description = models.CharField(max_length=1000)
	user = models.ForeignKey(User)	
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("CastlesPage")

class House(models.Model):
	name = models.CharField(max_length=80)
	slogan = models.CharField(max_length=80)
	castle = models.ManyToManyField(Castle)
	place = models.ForeignKey(Place)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("HousesPage")

class Person(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=80) 	
	civil_status = models.CharField(max_length=80)
	#father = models.ForeignKey(Person, related_name='Mother')
	#mother = models.ForeignKey(self, related_name='Father')
	house = models.ForeignKey(House)
	place = models.ForeignKey(Place)
	dead = models.BooleanField()
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("PersonsPage")

