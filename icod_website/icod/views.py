from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from icod.models import Home, Category

def index(request):
	context = RequestContext(request)
	intro_list = Home.objects.all()
	context_dict = {'intros' : intro_list}
	return render_to_response('icod/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)
	intro_list = Home.objects.all()
	context_dict = {'intros' : intro_list}
	return render_to_response('icod/about.html', context_dict, context)

def services(request):
	return HttpResponse("The services we provide!")

def teamMembers(request):
	return HttpResponse("Meet the team!")

def category(request):
	return HttpResponse("The News Categories")
