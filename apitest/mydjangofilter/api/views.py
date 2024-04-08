# from django.shortcuts import render
# from .models import Student
# from .serializer import StudentSerializer
# from rest_framework.generics import ListAPIView

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filterset_fields = ["city"]


from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["city"]
