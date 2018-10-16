from django.contrib import admin
from .models import *

# Register your models here.

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')





admin.site.register(Region,RegionAdmin)
admin.site.register(Comuna,ComunaAdmin)
