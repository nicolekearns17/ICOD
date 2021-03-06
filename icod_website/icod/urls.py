from django.conf.urls import patterns, url
from icod import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^services', views.services, name='services'),
	url(r'^team', views.teamMembers, name='team'),
	url(r'^category', views.category, name='category'),
	url(r'^member_info/(?P<member_name>\w+)', views.member_info, name='member_info'),
	url(r'^test', views.test, name='test'),
	url(r'^news', views.news, name='news'),
	url(r'^contact', views.contact, name='contact')

)
