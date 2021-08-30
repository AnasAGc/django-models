from django.contrib import admin

# Register your models here.

from .models import Snacks,Drinks
admin.site.register(Snacks)
admin.site.register(Drinks)