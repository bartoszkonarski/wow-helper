from django.contrib import admin

# Register your models here.
from .models import Raid, Raider

admin.site.register(Raid)
admin.site.register(Raider)
