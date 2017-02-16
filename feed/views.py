from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from models import Post

# Create your views here.
@login_required(login_url='/login/')
def posts(request):
	posts = Post.objects.all()
	#other_posts = Post.objects.filter(user_out=request.user)
	context = {"posts": posts}
	return render(request,"feed/index.html", context)

@login_required(login_url='/login/')
def test(request):
    return HttpResponse("Test successeded.")