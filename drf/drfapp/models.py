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
    
    
    
    
class Profile(models.model):
    
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media')
    dob=models.DateField()
    
    bio=models.TextField(max_length=100)
    
    def __str__(self):
        return self.user
        