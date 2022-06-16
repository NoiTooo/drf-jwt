from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('videos', views.VideoViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create')
]
