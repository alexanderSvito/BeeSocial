from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from models import Post

# Create your views here.
@login_required(login_url='/login/')
def posts(request):
	#posts = Post.objects.all()
	context = {}
	other_posts = [post for sub in request.user.subscribtions.all() for post in sub]
	#context["posts"] = posts
	context["other_posts"] = other_posts
 	return render(request,"feed/index.html", context)

@login_required(login_url='/login/')
def test(request):
    return HttpResponse("Test successeded.")