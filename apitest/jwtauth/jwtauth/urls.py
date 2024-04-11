from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView,TokenVerifyView

routes = DefaultRouter()

routes.register('api',views.StudentModelViewSet, basename="student")

urlpatterns = [
    path('gettoken/',TokenObtainPairView.as_view(),name="tokenobtain"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="tokenrefresh"),
    path('verifyview/',TokenVerifyView.as_view(),name="verifyuser"), # optional
    path('admin/', admin.site.urls),
    path('',include(routes.urls)),
]
