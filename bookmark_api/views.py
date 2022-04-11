from urllib import request
from crum import get_current_user
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from art_api.serializers import ArtSerializer
from bookmark import models
from bookmark.models import Bookmark
from users.models import NewUser
from .serializers import BookmarkSerializer
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
class BookmarkArt(APIView):
    serializer_class = BookmarkSerializer
    # queryset = Bookmark.objects.all()
    
    def post(self,request,art_id,format=None):
        # bookmark = Bookmark.objects.get()    

        user_id = self.request.user.id

        if models.Bookmark.objects.filter(art=art_id, user=user_id):  
            print(art_id)
            
            models.Bookmark.objects.filter(art=art_id, user=user_id).delete()
            return HttpResponse('Found')
        else:     
            data = { 'user': user_id, 'art': art_id }
            serializer = BookmarkSerializer(data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return HttpResponse('NotFound')

            
                
                
                
               