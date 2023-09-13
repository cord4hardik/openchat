from django.contrib import admin
from .models import Group, Message


@admin.register(Group)
class MyModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'group')