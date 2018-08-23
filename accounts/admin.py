from django.contrib import admin
from accounts.models import User, Group

# Register your models here.
admin.site.register(Group)
admin.site.register(User)
