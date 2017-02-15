from __future__ import unicode_literals
from django.db import models
from users.models import User

class Dialog(models.Model):
	"""docstring for Dialog"""
	name = models.CharField(max_length=140)
	started_at = models.DateTimeField(auto_now_add=True)
	participants = models.ManyToManyField(User, related_name="dialogs")

	def __str__(self):
		return self.name
	
class Message(models.Model):
	"""docstring for Message"""
	dialog = models.ForeignKey(Dialog, related_name="messages", on_delete=models.CASCADE)
	author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
	text = models.CharField(max_length=256)
	sent_at = models.DateTimeField(auto_now_add=True)
