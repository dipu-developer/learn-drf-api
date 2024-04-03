from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]  # Use BasicAuthentication
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser] # only allw the is_staff = True
    permission_classes = [DjangoModelPermissions] # we have to provide the permission on admin pannel

# to user the session page must include to this line in urls.py so that you have an option to login 
    

    # path('auth/',include('rest_framework.urls',namespace='rest_framework'))
