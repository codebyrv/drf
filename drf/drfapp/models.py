from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.name
    
    
    
    
    