from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]  # Use BasicAuthentication
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser] # only allw the is_staff = True

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]  # Use BasicAuthentication
#     permission_classes = [AllowAny]


# to provide the authentication globely write this code in settin.py in the last
 # settings.py

# we can also overwite the code by include the allow any those code is by default work

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#         # Add other authentication classes if needed
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#         # Add other permission classes if needed
#     ],
#     # Other Django REST Framework settings...
# }
