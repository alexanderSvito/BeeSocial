from __future__ import unicode_literals
from users.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	text = models.CharField(max_length=140)
	started_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, related_name="posts")
	