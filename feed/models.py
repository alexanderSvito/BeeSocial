from __future__ import unicode_literals
from users.models import User
from django.db import models
from bee_social.models import Base

# Create your models here.
class Post(Base):
	"""docstring for Post"""
	text = models.CharField(max_length=140)
	user = models.ForeignKey(User, related_name="posts")
	