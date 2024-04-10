from rest_framework import serializers
from .models import Song, Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','duration','singer']

class SingerSerializer(serializers.ModelSerializer):
    slub = SongSerializer(many = True, read_only = True, source= "singer")
    class Meta:
        model = Singer
        fields = ['id','name','gender', 'slub'] 
