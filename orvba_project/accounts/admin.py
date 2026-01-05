from django.contrib import admin
from .models import CustomUser, MechanicProfile

admin.site.register(CustomUser)
admin.site.register(MechanicProfile)

