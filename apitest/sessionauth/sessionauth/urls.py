from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

routes = DefaultRouter()

routes.register('api',views.StudentModelViewSet, basename="student")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routes.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
