from django.contrib import admin
from .models import vehicle_service,vehicle_serviceAdmin
admin.site.register(vehicle_service,vehicle_serviceAdmin)