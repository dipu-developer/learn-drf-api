from django.shortcuts import render
from .models import Singer,Song
from .serializers import SongSerializer, SingerSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer



