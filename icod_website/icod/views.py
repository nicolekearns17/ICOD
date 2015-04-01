from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from icod.models import Home, Category, TeamMember
from django.http import HttpResponseRedirect

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
	context = RequestContext(request)
	team_info = TeamMember.objects.all()
	context_dict = {'teamMembers' : team_info}
	return render_to_response('icod/team.html', context_dict, context)

def test(request):
	context = RequestContext(request)
	intro_list = Home.objects.all()
	context_dict = {'intros' : intro_list}
	return render_to_response('icod/test.html', context_dict, context)

def news(request):
	context = RequestContext(request)
	return render_to_response('icod/news.html', context)

def category(request):
	return HttpResponse("The News Categories")

def member_info(request, member_name):
	template = loader.get_template('icod/member_info.html')
	person = TeamMember.objects.get(name__contains=member_name)
	context_dict = {'member' : person}
	context = RequestContext(request,context_dict)
	return HttpResponse(template.render(context))
