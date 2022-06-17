from django.http import Http404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from .models import Video
from .serializers import VideoSerializer, UserSerializer

User = get_user_model()

class AdminOnlyUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if str(self.request.user.pk) == str(self.kwargs['pk']):
            return self.retrieve(request, *args, **kwargs)        
        else:
            raise Http404("can not access")
            

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
