from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Place(models.Model):

	name = models.CharField(max_length=80)
	description = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.name

class Castle(models.Model):
	name = models.CharField(max_length=80)
	place = models.ForeignKey(Place)
	description = models.CharField(max_length=1000)
		
	def __unicode__(self):
		return self.name

class House(models.Model):
	name = models.CharField(max_length=80)
	slogan = models.CharField(max_length=80)
	castle = models.ManyToManyField(Castle)
	place = models.ForeignKey(Place)
	
	def __unicode__(self):
		return self.name

class Person(models.Model):

	name = models.CharField(max_length=80) 	
	#father = models.ForeignKey(Person, related_name='Mother')
	#mother = models.ForeignKey(self, related_name='Father')
	house = models.ForeignKey(House)
	place = models.ForeignKey(Place)
	dead = models.BooleanField()
	def __unicode__(self):
		return self.name

class Review(models.Model):
	RATING_CHOICES = ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'))
	rating = models.PositiveSmallIntegerField('Rating (stars)',blank=False, default=3, choices=RATING_CHOICES)
	comment = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, default=User.objects.get(id=1))
	date = models.DateField(default=date.today)

	class Meta:
		abstract = True

class PersonReview(Review):
	person = models.ForeignKey(Person)
