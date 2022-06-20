from django.contrib import admin
from .models import Project

# Register your models here.
class projectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Project,projectAdmin)


