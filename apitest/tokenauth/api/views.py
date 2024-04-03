from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer

class StudentMVS(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# INSTALLED_APPS = [
#     'rest_framework',
#     'rest_framework.authtoken',     #to use add token feature
#     'api',
# ]


# from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns = [
#     path('token/',obtain_auth_token),
# ]