from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	"""docstring for User"""
	email = models.EmailField()
	subscribtions = models.ManyToManyField("self", blank=True, symmetrical=False)
	blacklist = models.ManyToManyField("self", blank=True)
	
		
class Account(models.Model):
	"""docstring for Account"""
	avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/")
	user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE, primary_key=True)