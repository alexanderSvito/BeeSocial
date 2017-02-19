from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from models import User, Dialog

@login_required(login_url='/login/')
def index(request):
    request.dialogs = request.user.dialogs.all()
    return render(request, 'index.html')

@login_required(login_url='/login/')
def messages(request, id):
    arr = request.user.dialogs.get(id=id).messages.all()
    return JsonResponse([message.as_json() for message in arr], safe=False)

@login_required(login_url='/login/')
def dialogs(request):
    arr = request.user.dialogs.all()
    return JsonResponse([dialog.as_json() for dialog in arr], safe=False)