from django.db import models

# Create your models here.

class Person(models.Model):

	name = models.CharField(max_length=80)
	familiars = [] 	
	#house = models.ForeignKey(House)
	#place = models.ForeignKey(Place)

class House(models.Model):

	name = models.CharField(max_length=80)

#class Place(models.Model):

	#name = models.CharField(max_length=80)
