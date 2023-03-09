from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubDistrict(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name +' - ' + self.district

class Village(models.Model):
    name = models.CharField(max_length=100)
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.subdistrict

class Department(models.Model):
    
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - '+self.subdistrict+' - '+self.district
    
class Group(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):

    fname = models.CharField(max_length=200,) 
    lname = models.CharField(max_length=200,) 
    gender = models.CharField(max_length=10) 
    address = models.TextField() 
    position = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    status = models.IntegerField() 
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname + ' - '+self.lname + ' - '+ str(self.phone_number)

class Job(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='job_images/')
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=155)
    lname = models.CharField(max_length=155)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    mister_pop = models.BooleanField(default=False)
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname + ' - ' + self.lname +' - '+ str(self.phone_number)