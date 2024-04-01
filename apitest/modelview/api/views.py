from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):   # we can perform all varoius operations all CRUD
    queryset = Student.objects.all()
    serializer_class = StudentSerializer