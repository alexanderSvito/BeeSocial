from django.contrib import admin
from .models import User, Account, Dialog, Message

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Dialog)
admin.site.register(Message)