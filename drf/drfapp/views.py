from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView

from drfapp.models import*

# from drfapp.serializers import StudentSerializer
from drfapp.serializers import StudentModelSerializers

from rest_framework import status
# Create your views here.
class HelloApi(APIView):
    def get(self,request):
        return Response({"message":"hello DRF"})
    
    
# class StudentView(APIView):
#     def get(self,request):
#         try:
#             student=Student.objects.all()        
#             serializer=StudentSerializer(student,many=True)
#             return Response(data=serializer.data)
        
#         except:
            
#             return Response({"msg":"no data avaialble"})
        
#     def delete(self,request):
#         try:
#             student=Student.objects.all().delete()
#             # student.delete()
#             return Response({"msg":"all data deleted"})
#         except: 
#             return Response({"msg":"matching query doesnot exists"},status=status.HTTP_404_NOT_FOUND)

#     def post(self,request,*args, **kwargs):
#         # Serializer=StudentSerializer(data=request.data)
#         name=request.data.get("name")  
#         dob=request.data.get("dob")  
#         age=request.data.get("age")  
#         place=request.data.get("place")
#         student=Student.objects.create(name=name,dob=dob,age=age,place=place)
#         return Response({"data":"data added successfully"},status=status.HTTP_200_OK)
   
# class StudentDetailView(APIView):  
#     def get(self,request,id): 
#         try:
#             student=Student.objects.get(id=id)
#             serializer=StudentSerializer(student)
#             return Response(data=serializer.data)
#         except:  
#             return Response({'invalid data'},status=status.HTTP_404_NOT_FOUND)
#     def delete(self,request,id):
#         try:
#             student=Student.objects.get(id=id)
#             student.delete()
#             return Response({"msg":"data deleted"})
#         except: 
#             return Response({"msg":"matching query doesnot exists"},status=status.HTTP_404_NOT_FOUND)
    
        
#     def put(self,request,id):
#         try:
#            student=Student.objects.get(id=id) 
#            name=request.data.get("name")
#            dob=request.data.get("dob")
#            age=request.data.get("age")
#            place=request.data.get("place")
#            student.name=name
#            student.dob=dob
#            student.age=age  
#            student.place=place
#            student.save()
           
#            return Response({"msg":"updated successfully"})
#         except:  
#            return Response({"msg":"not matching"}) 
        
           
           
#class Using Modelserializer           

class StudentModelView(APIView):
    def get(self,reqeust,*args, **kwargs):
        try:
            student=Student.objects.all()
            serailzer=StudentModelSerializers(student,many=True)
            return Response(data=serailzer.data)
        except:
            return Response({"msg":"no data available"})
    def post(self,request,*args, **kwargs):
        try:
            serializer=StudentModelSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({"msg":"data createdd"})
        except:
            return Response({"msg":"error"})    
class StudentModelDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serialzer=StudentModelSerializers(student)
        return Response(data=serialzer.data)
    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentModelSerializers(data=request.data,instance=student)
        if serializer.is_valid():
            serializer.save()
        return Response({"msg":"student updated"})
    def delete(self,request,id):
        try:
            student=Student.objects.get(id=id)
            student.delete()
            return Response({"msg":"deleted"})
        except:  
            return Response({"msg":"no data there for delete"})

    
    
    
    
    
        
                  