from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .limtoffset import MyCustomLimitPagination

# PageNumberPagination
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#LimitOffsetPagination
class StudentList(ListAPIView):     #http://127.0.0.1:8000/api/?offset=5&page=2
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCustomLimitPagination
    
