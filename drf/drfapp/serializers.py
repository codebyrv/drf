from rest_framework import serializers

from drfapp.models import Student


# class StudentSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     dob=serializers.DateField()
#     age=serializers.IntegerField()
#     place=serializers.CharField()
    
from django.contrib.auth.models import User    
    
class StudentModelSerializers(serializers.ModelSerializer):
    
    
    class Meta:
        model=Student
        fields="__all__"
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        
                