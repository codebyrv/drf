from rest_framework import serializers



class StudentSerializer(serializers.Serializer):
    
    name=serializers.CharField()
    dob=serializers.DateField
    age=serializers.IntegerField()
    place=serializers.CharField()
    