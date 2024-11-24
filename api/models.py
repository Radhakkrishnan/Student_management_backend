from django.db import models

# Create your models here.
class Student(models.Model):

   
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    DateOfBirth = models.DateField(max_length=50)
    Gender = models.CharField(max_length=100)
    BloodGroup = models.CharField(max_length=50)
    ContactNo = models.IntegerField(default=1234567890)
    Address = models.CharField(max_length=500)

    
