
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from users.models import NewUser
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticated]
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer


class ListAllArtistUser(generics.ListAPIView):
    queryset = NewUser.artist_object.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer