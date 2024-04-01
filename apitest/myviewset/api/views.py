from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet (viewsets.ViewSet):
    def list(self,request):
        print("Basename: ",self.basename)
        print("action: ",self.action)
        print("Suffix: ",self.suffix)
        print("details: ",self.detail)
        print("Name: ",self.name)
        print("Discription: ",self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    def retrieve (self , request, pk = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    def create (self, request):
        stu = StudentSerializer(data = request.data)
        if stu.is_valid():
            stu.save()
            return Response({"msg":"Data add Sucessfully"})
        return Response(stu.error, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk):
        stu = Student.objects.get(id = pk )
        serializer = StudentSerializer(stu,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updata Sucessfully"})
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({"Msg":"Data is delete"})

