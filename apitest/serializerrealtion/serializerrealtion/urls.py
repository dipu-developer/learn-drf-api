from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('song',views.SongView,basename='song')
router.register('singer',views.SingerView,basename='singer')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),

]
