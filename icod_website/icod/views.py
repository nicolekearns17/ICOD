from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from icod.models import Home, Category, TeamMember, NewsItem
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
	news_list = NewsItem.objects.all().order_by('date')
	fin_list = NewsItem.objects.filter(category__name='Financial').order_by('date')
	recog_list = NewsItem.objects.filter(category__name='Recognition').order_by('date')
	pol_list = NewsItem.objects.filter(category__name='Policy Changes').order_by('date')
	soc_list = NewsItem.objects.filter(category__name='Social News').order_by('date')
	context_dict = {'news' : news_list, 'fin' : fin_list, 'recog': recog_list, 'pols' : pol_list, 'socs' : soc_list}
	return render_to_response('icod/news.html', context_dict, context)

def category(request):
	return HttpResponse("The News Categories")

def member_info(request, member_name):
	template = loader.get_template('icod/member_info.html')
	person = TeamMember.objects.get(name__contains=member_name)
	context_dict = {'member' : person}
	context = RequestContext(request,context_dict)
	return HttpResponse(template.render(context))

def contact(request):
	context = RequestContext(request)
	return render_to_response('icod/contact.html',context)
