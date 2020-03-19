from django.contrib import admin
from .models import ToDo
# Register your models here.
@admin.register(ToDo)
class ToDoModelAdmin(admin.ModelAdmin):
    pass