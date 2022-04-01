from urllib import request
from crum import get_current_user
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from art import models
from art.models import Art
from bookmark_api.serializers import BookmarkSerializer
from users.models import NewUser
from .serializers import ArtSerializer
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
# class ArtList(generics.ListCreateAPIView):  
#     queryset = Art.objects.all()
#     serializer_class = ArtSerializer

# @csrf_exempt
# def LikeView(self,request, art_id):
#     permission_classes = [IsAuthenticated]

#     if request.method == 'POST':
#         # recieve post data
#         art = get_object_or_404(Art, id=art_id)
#         user_id = self.request.user.id
#         print(user_id)
#         art.likes.add(user_id)

        
#         return HttpResponse('Value recorded')
#     else:
#         return HttpResponse('Value Not recorded')

class LikeView(APIView):
    def post(self,request,art_id):
        
        art = get_object_or_404(Art,id=art_id)
        user_id = self.request.user.id
        
        if models.Art.likes.through.objects.filter(art_id=art_id, newuser_id=user_id):  
            print(user_id)
            # art.likes.add(user_id)
            models.Art.likes.through.objects.filter(art_id=art_id, newuser_id=user_id).delete()
            return HttpResponse('Found')
        else:
            art.likes.add(user_id)
            return HttpResponse('NotFound')


class CreateArt(APIView):
    permission_classes = [IsAuthenticated]
    # queryset = Art.objects.all()
    # serializer_class = ArtSerializer()
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        print(request.data)
        if request.method == 'POST':
            serializer = ArtSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtDetails(generics.ListAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        print(id)
        return Art.objects.filter(slug=id)

class ArtDetail(generics.ListAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        slug = self.kwargs['pk']
        print(slug)
        return Art.objects.filter(slug=slug)

class ListUserArtPost(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Art.objects.filter(user=get_current_user())
    serializer_class = ArtSerializer

    def get_queryset(self):
        user = self.request.user
        return Art.objects.filter(user=user)

class PostListDetailFilter(generics.ListAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$slug']

    # '^' - Starts with search 
    # '=' - Exact matches
    # '@' - Full-text matches
    # '$' - Regex matches

class RetrieveAllArtPost(generics.ListAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

class AbstractGenreArtFilter(generics.ListAPIView):
    serializer_class = ArtSerializer
    def get_queryset(self):
        genre = self.kwargs['genre']
        return Art.objects.filter(genre=genre)

class BookmarkArt(APIView):
    serializer_class = ArtSerializer

    def post(self,request,art_id):
        
        art = get_object_or_404(Art,id=art_id)
        user_id = self.request.user.id

        if models.Art.bookmarks.through.objects.filter(art_id=art_id, newuser_id=user_id):  
            print(user_id)
            models.Art.bookmarks.through.objects.filter(art_id=art_id, newuser_id=user_id).delete()
            return HttpResponse('Found')
        else:
            art.bookmarks.add(user_id)
            return HttpResponse('NotFound')
    


class GetBookmarkArtView(generics.ListAPIView):
    serializer_class = ArtSerializer
    def get_queryset(self):
        
        user_id = self.request.user.id
        
        
        return Art.objects.filter(bookmark__user=user_id).all()

      

