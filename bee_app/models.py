from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class Dialog(models.Model):
	"""docstring for Dialog"""
	name = models.CharField(max_length=140)
	started_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class User(AbstractUser):
	"""docstring for User"""
	email = models.EmailField()
	subscribtions = models.ManyToManyField("self", blank=True, symmetrical=False)
	blacklist = models.ManyToManyField("self", blank=True)
	dialogs = models.ManyToManyField(Dialog, related_name="participants", blank=True)
		
class Account(models.Model):
	"""docstring for Account"""
	avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/")
	user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE, primary_key=True)
	

class Message(models.Model):
	"""docstring for Message"""
	dialog = models.ForeignKey(Dialog, related_name="messages", on_delete=models.CASCADE)
	author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
	text = models.CharField(max_length=256)
	sent_at = models.DateTimeField(auto_now_add=True)