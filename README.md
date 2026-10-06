# Ex02 Django ORM Web Application
## Date: 06.10.26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import vehicle_service,vehicle_serviceAdmin
admin.site.register(vehicle_service,vehicle_serviceAdmin)

```


## OUTPUT
![alt text](image.png)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
