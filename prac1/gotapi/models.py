from django.db import models

# Create your models here.


class House(models.Model):

	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Place(models.Model):

	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Person(models.Model):

	
	name = models.CharField(max_length=80)
	familiars = [] 	
	house = models.ForeignKey(House)
	place = models.ForeignKey(Place)
	def __unicode__(self):
		return self.name
