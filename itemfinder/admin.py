from django.contrib import admin

# Register your models here.
from .models import Leather,Cloth,Mail,Plate,Other,Trinket
admin.site.register(Cloth)
admin.site.register(Leather)
admin.site.register(Mail)
admin.site.register(Plate)
admin.site.register(Other)
admin.site.register(Trinket)

