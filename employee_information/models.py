from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employees(models.Model):

    firstname = models.CharField(max_length=200,) 

    lastname = models.CharField(max_length=200,) 
    gender = models.CharField(max_length=200, blank=True,null=True) 

    contact = models.CharField(max_length=200,) 
    address = models.CharField(max_length=200,) 

    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 

    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' - '+self.lastname + ' '