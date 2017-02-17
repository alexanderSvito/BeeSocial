from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from models import User, Dialog

@login_required(login_url='/login/')
def test(request):
    return HttpResponse("Test successeded.")

@login_required(login_url='/login/')
def dialogs(request):
    request.dialogs = request.user.dialogs.all()
    return render(request, 'index.html')

@login_required(login_url='/login/')
def messages(request, id):
    arr = request.user.dialogs.get(id=id).messages.all()
    return JsonResponse([msg.as_json() for msg in arr], safe=False)