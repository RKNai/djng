from django.forms import ModelForm
from models import *

class PersonForm(ModelForm):
	class Meta:
		model = Person

class PlaceForm(ModelForm):
	class Meta:
		model = Place

class CastleForm(ModelForm):
	class Meta:
		model = Castle

class HouseForm(ModelForm):
	class Meta:
		model = House

class RealplaceForm(ModelForm):
	class Meta:
		model = Realplace
