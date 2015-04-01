from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from icod.models import Home, Category, TeamMember

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

def category(request):
	return HttpResponse("The News Categories")

#def user_profiles(request, name):
#		currentUser=request.user.username
#		cat_list = Category.objects.all()
#		posts_list=Post.objects.all().order_by('-id')
#		comments_list=postComment.objects.all().order_by('-id')
#		links=Link.objects.all()
#		if not request.user.is_authenticated():
#			HttpResponseRedirect('/login/')
#		userSearched=User.objects.get(username=name)
#		followingList =Followers.objects.filter(fuser=request.user).values_list('follows', flat=True)
#		p=UserProfile.objects.get(user=userSearched)
#		picture=p.picture
#		posts=Post.objects.filter(userProfile=p)
#		context = RequestContext(request,{'followingList':followingList, 'currentUser':currentUser, 'picture':picture, 'user1': userSearched, 'cat_list': cat_list, 'posts_list':posts,'comments_list':comments_list,'links':links})
#		return render_to_response('shareit/profile.html', {}, context )
