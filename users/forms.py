from django import forms
from bee_app.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()


    class Meta(object):
    	model = User
        fields = ('email', 'username')
    	