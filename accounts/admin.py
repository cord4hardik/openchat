from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'phone_number', 'is_active', 'is_superuser')