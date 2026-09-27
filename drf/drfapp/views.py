from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView

from drfapp.models import*

from drfapp.serializers import StudentSerializer
# Create your views here.


class HelloApi(APIView):

    def get(self,request):
        
        return Response({"message":"hello DRF"})



class StudentView(APIView):
    def get(self,request):
        
        student=Student.objects.all()
        
        serializer=StudentSerializer(student,many=True)
        
        return Response(data=serializer.data)

    def post(self,request,*args, **kwargs):
        
        # Serializer=StudentSerializer(data=request.data)
        
        name=request.data.get("name")  
        dob=request.data.get("dob")  
        age=request.data.get("age")  
        place=request.data.get("place")

        
        student=Student.objects.create(name=name,dob=dob,age=age,place=place)
        
        return Response({"data":"data added successfully"})
    
    