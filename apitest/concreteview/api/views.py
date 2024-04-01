from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrive(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpudate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# We can use Instence of this

class StudentLC(ListCreateAPIView):     #This get all and create
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRUD(RetrieveUpdateDestroyAPIView): #single data updata, get and delete
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    