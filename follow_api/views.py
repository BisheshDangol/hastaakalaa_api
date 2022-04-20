from urllib import request
from crum import get_current_user
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from art.models import Art
from art_api.serializers import ArtSerializer
from follow import models
from follow.models import Follow
from users.models import NewUser
from .serializers import FollowSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework.generics import GenericAPIView

# Create your views here.

# @csrf_exempt
class FollowUser(APIView):
    serializer_class = FollowSerializer
    # queryset = Bookmark.objects.all()
    
    def post(self,request,follower,format=None):
        # bookmark = Bookmark.objects.get()    

        user_id = self.request.user.id

        if models.Follow.objects.filter(user_id=user_id, follower_id=follower):  
            print(follower)
            
            models.Follow.objects.filter(user_id=user_id, follower_id=follower).delete()
            return HttpResponse('Found')
        else:     
            data = { 'user_id': user_id, 'follower_id': follower }
            serializer = FollowSerializer(data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return HttpResponse('NotFound')
            
class GetFollowingList(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Follow.objects.filter(user_id=user)

class GetFollowerList(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Follow.objects.filter(follower_id=user)

class AllList(generics.ListAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    

class OtherFollowerList(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        print(id)
        return Follow.objects.filter(follower_id=id)


class OtherFollowingList(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        print(id)
        return Follow.objects.filter(user_id=id)
               