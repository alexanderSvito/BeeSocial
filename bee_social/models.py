from __future__ import unicode_literals
from users.models import User
from django.db import models

class Base(models.Model):
    """docstring for Base"""

    started_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
