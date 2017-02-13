from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from models import User, Dialog
from helpers import jsonfy_messages

def index(request):
    return HttpResponse("Hello, world.")

@login_required(login_url='/login/')
def test(request):
    return HttpResponse("Test successeded.")

@login_required(login_url='/login/')
def dialogs(request):
    request.dialogs = request.user.dialogs.all()
    return render(request, 'messages/index.html')

@login_required(login_url='/login/')
def messages(request, id):
    arr = request.user.dialogs.get(id=id).messages.all()
    return JsonResponse(jsonfy_messages(arr), safe=False)