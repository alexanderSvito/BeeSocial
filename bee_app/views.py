from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world.")

@login_required(login_url='/login/')
def test(request):
    return HttpResponse("Test successeded.")

@login_required(login_url='/login/')
def messages(request):
    return render(request, 'messages/index.html')