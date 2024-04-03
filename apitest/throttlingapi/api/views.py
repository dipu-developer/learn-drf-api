from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from .thorttling import JackRateThrottle


# class StudentMVS(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     throttle_classes= [AnonRateThrottle,UserRateThrottle]


class StudentMVS(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes= [JackRateThrottle]


# REST_FRAMEWORK = {
#     'DEFAULT_THROTTLE_CLASSES': (
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle',
#     ),
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '100/day',  # Throttle rate for anonymous users
#         'user': '1000/day',  # Throttle rate for authenticated users
#     },
# }