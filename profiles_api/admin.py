from django.contrib import admin
from .models import UserProfile, UserFeed

admin.site.register(UserProfile)
admin.site.register(UserFeed)