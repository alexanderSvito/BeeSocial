from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from models import Post

# Create your views here.
@login_required(login_url='/login/')
def posts(request):
    self_posts = Post.objects.filter(user_id=request.user)
    other_posts = Post.objects.filter(user_id__in=[user for user in request.user.subscribtions.all()])
    context = {}
    context["posts"] = self_posts
    context["other_posts"] = other_posts
    return render(request,"feed/index.html", context)

@login_required(login_url='/login/')
def test(request):
    return HttpResponse("Test successeded.")