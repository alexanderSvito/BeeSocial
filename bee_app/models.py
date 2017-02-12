from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Dialog(models.Model):
	"""docstring for Dialog"""
	started_at = models.DateTimeField(auto_now_add=True)
			
class Account(models.Model):
	"""docstring for Account"""
	avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/")
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	subscribtions = models.ManyToManyField("self", blank=True, symmetrical=False)
	blacklist = models.ManyToManyField("self", blank=True)
	dialogs = models.ManyToManyField(Dialog, related_name="participants", blank=True)

class Message(models.Model):
	"""docstring for Message"""
	dialog = models.ForeignKey(Dialog, related_name="messages", on_delete=models.CASCADE)
	user = models.ForeignKey(Account, related_name="messages", on_delete=models.CASCADE)
	text = models.CharField(max_length=256)
	sent_at = models.DateTimeField(auto_now_add=True)