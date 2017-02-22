from __future__ import unicode_literals
from django.db import models
from users.models import User
from bee_social.models import Base

class Dialog(Base):
	"""docstring for Dialog"""
	name = models.CharField(max_length=140)
	participants = models.ManyToManyField(User, related_name="dialogs")

	def preview(self):
		return self.messages.reverse()[0].text

	def as_json(self):
		return {"name": self.name, "preview": self.preview(), "id": self.id}

	def __str__(self):
		return self.name
	
class Message(models.Model):
	"""docstring for Message"""
	dialog = models.ForeignKey(Dialog, related_name="messages", on_delete=models.CASCADE)
	author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
	text = models.CharField(max_length=256)
	sent_at = models.DateTimeField(auto_now_add=True)

	def as_json(self):
		return {'author': str(self.author), 'text': self.text, 'sent_at': self.sent_at}

	def __str__(self):
		return "Msg from %s: %s" % (self.author, self.text)
