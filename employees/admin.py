from django.contrib import admin
from .models import Employee

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', )

admin.site.register(Employee, TaskAdmin)