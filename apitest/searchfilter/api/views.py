from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city'] # we can only use the single query
    # search_fields = ['name','city'] # we can filter both query
    search_fields = ['^name'] # we can filter start with name singl letter
