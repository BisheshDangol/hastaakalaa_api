
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from users.models import NewUser
from .models import NewUser as user_model
from rest_framework.permissions import IsAuthenticated
from users import models

class CustomUserCreate(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer

    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAllUser(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer

class GetCurrentUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        user = self.request.user.id
        return NewUser.objects.filter(id=user)



class ListAllArtistUser(generics.ListAPIView):
    queryset = NewUser.artist_object.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer

class FollowView(APIView):
    def post(self,request,user_id):  
        users = get_object_or_404(user_model, id=user_id)
        gottenuser = self.request.user.id
        print(gottenuser)
        print(user_id)
        if models.NewUser.follower.through.objects.filter(from_newuser_id=user_id, to_newuser_id=gottenuser):  
            
            models.NewUser.follower.through.objects.filter(from_newuser_id=user_id, to_newuser_id=gottenuser).delete()
            return HttpResponse('Value found was found and deleted')
        else:
            users.follower.add(gottenuser)
            return HttpResponse('Value was not found. Value is now created')


class FollowedView(APIView):
    def post(self,request,user_id):  
        users = get_object_or_404(user_model, id=user_id)
        gottenuser = self.request.user.id
        print(gottenuser)
        print(user_id)
        if models.NewUser.followedby.through.objects.filter(from_newuser_id=user_id, to_newuser_id=gottenuser):  
            
            models.NewUser.followedby.through.objects.filter(from_newuser_id=user_id, to_newuser_id=gottenuser).delete()
            return HttpResponse('Value found was found and deleted')
        else:
            users.followedby.add(gottenuser)
            return HttpResponse('Value was not found. Value is now created')