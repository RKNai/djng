from django.conf.urls import patterns, include, url
from gotapi.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^characters/$', characterspage, name = 'PersonsPage'),
    url(r'^houses/$', housespage, name = 'HousesPage'),
    url(r'^places/$', placespage, name = 'PlacesPage'),
    url(r'^castles/$', castlespage, name = 'CastlesPage'),
    url(r'^characters/(?P<idaux>\d+)/$', singlecharacterpage),
    url(r'^houses/(?P<idaux>\d+)/$', singlehousepage),
    url(r'^castles/(?P<idaux>\d+)/$', singlecastlepage),
    url(r'^places/(?P<idaux>\d+)/$', singleplacepage),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^characters/create/$',CreatePerson.as_view(),name='CreatePerson'),
    url(r'^castles/create/$',CreateCastle.as_view(),name='CreateCastle'),
    url(r'^places/create/$',CreatePlace.as_view(),name='CreatePlace'),
    url(r'^houses/create/$',CreateHouse.as_view(),name='CreateHouse'),
    url(r'^places/(?P<pk>\d+)/edit/$', UpdateView.as_view( model = Place, template_name = 'forms.html', form_class = PlaceForm), name='place_edit'),
    url(r'^characters/(?P<pk>\d+)/edit/$', UpdateView.as_view( model = Person, template_name = 'forms.html', form_class = PersonForm), name='person_edit'),
    url(r'^castles/(?P<pk>\d+)/edit/$', UpdateView.as_view( model = Castle, template_name = 'forms.html', form_class = CastleForm), name='castle_edit'),
    url(r'^houses/(?P<pk>\d+)/edit/$', UpdateView.as_view( model = House, template_name = 'forms.html', form_class = HouseForm), name='house_edit'),
    url(r'^castles/(?P<pk>\d+)/delete/$', DeleteView.as_view( model = Castle, template_name = 'delete.html', success_url = '/castles/')),
    url(r'^houses/(?P<pk>\d+)/delete/$', DeleteView.as_view( model = House, template_name = 'delete.html', success_url = '/houses/')),
    url(r'^characters/(?P<pk>\d+)/delete/$', DeleteView.as_view( model = Person, template_name = 'delete.html', success_url = '/characters/')),
    url(r'^places/(?P<pk>\d+)/delete/$', DeleteView.as_view( model = Place, template_name = 'delete.html', success_url = '/places/')),
    # url(r'^$', 'prac1.views.home', name='home'),
    # url(r'^prac1/', include('prac1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

