from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^resources', views.resources, name='map-resources'), 
	url(r'^contact', views.contact, name='map-contact'),
	url(r'^about', views.about, name='map-about'),
	url(r'^download', views.download, name='map-download'),
	url(r'^$', views.home, name='map-home'),
	]