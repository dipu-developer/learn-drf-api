from rest_framework import serializers
from .models import Song, Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','duration','singer']

class SingerSerializer(serializers.ModelSerializer):
    # singer= serializers.StringRelatedField(many = True, read_only = True)
    # {
    #     "id": 3,
    #     "name": "Allu Arjun",
    #     "gender": "Male",
    #     "singer": [
    #         "paggi mali"
    #     ]
    # }
    # singer = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='singer-detail')
    #  {
    #     "id": 1,
    #     "name": "Arjit Sing",
    #     "gender": "male",
    #     "singer": [
    #         "http://127.0.0.1:8000/api/singer/1/",
    #         "http://127.0.0.1:8000/api/singer/4/"
    #     ]
    # },
    singer = serializers.SlugRelatedField(many = True, read_only = True, slug_field='duration') #slug field must me filed name
    # {
    #     "id": 1,
    #     "name": "Arjit Sing",
    #     "gender": "male",
    #     "singer": [
    #         3,
    #         3
    #     ]
    # },
    class Meta:
        model = Singer
        fields = ['id','name','gender','singer']
