from django.shortcuts import render
from forms import RegistrationForm
from django.views.decorators.csrf import csrf_protect
   
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/complete')

    else:
        form = RegistrationForm()
    token = {}
    #token.update(csrf(request))
    token['form'] = form

    return render(request, 'registration/registration_form.html', token)

def registration_complete(request):
    return render(request, 'registration/registration_complete.html')