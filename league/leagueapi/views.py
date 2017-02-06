from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, authentication, permissions
from .serializers import UserSerializer, GroupSerializer, ChampionSerializer
from django.http import HttpResponse

from .models import Champion

User = get_user_model()

class DefaultMixin(object):
    """Default settings for view authentication, permission, filtering, and pagination"""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ChampionViewSet(viewsets.ModelViewSet):
    """Api Endpoint for Champions"""
    queryset = Champion.objects.all()
    serializers_class = ChampionSerializer

def index(request):
    return HttpResponse('<h1>Sup playas</h1>')
