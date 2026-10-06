from django.db import models
from django.contrib import admin
class vehicle_service(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=35)
    customer_no=models.IntegerField()
    vehicle_no=models.CharField(max_length=15)
    email=models.EmailField()
    date=models.DateField()
    cost=models.FloatField()

class vehicle_serviceAdmin(admin.ModelAdmin):
    list_display=['customer_id','customer_name','customer_no','vehicle_no','email','date','cost']