## -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#
#from django.shortcuts import render
#
## Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet( viewsets.ModelViewSet ):
	''' API endpoint that allows users to be viewed or edited. '''
	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	queryset = User.objects.all().order_by( '-date_joined' )
	serializer_class = UserSerializer
	
class GroupViewSet( viewsets.ModelViewSet ):
	''' API endpoint that allows groups to be viewed and edited. '''
	
	queryset = Group.objects.all()
	serilaizer_class = GroupSerializer
