from django.db import models

# Create your models here.

class Place(models.Model):

	name = models.CharField(max_length=80)
	def __unicode__(self):
		return self.name

class Castle(models.Model):
	name = models.CharField(max_length=80)

class House(models.Model):
	name = models.CharField(max_length=80)
	slogan = models.CharField(max_length=80)
	place = models.ForeignKey(Place)
	
	def __unicode__(self):
		return self.name

class Person(models.Model):

	name = models.CharField(max_length=80) 	
	#father = models.ForeignKey(Person, related_name='Mother')
	#mother = models.ForeignKey(self, related_name='Father')
	house = models.ForeignKey(House)
	place = models.ForeignKey(Place)
	def __unicode__(self):
		return self.name
