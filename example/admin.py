from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time']