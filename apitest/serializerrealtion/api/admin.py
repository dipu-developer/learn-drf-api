from django.contrib import admin
from .models import Song,Singer
# Register your models here.
@admin.register(Singer)
class SingerAdminModel(admin.ModelAdmin):
    list_display = ['id','name','gender']

@admin.register(Song)
class SingerAdminModel(admin.ModelAdmin):
    list_display = ['id','title','duration']