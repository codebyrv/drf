from rest_framework import serializers



class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    dob=serializers.DateField()
    age=serializers.IntegerField()
    place=serializers.CharField()
    