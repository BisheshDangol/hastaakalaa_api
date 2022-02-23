from rest_framework import generics
from art.models import Art
from .serializers import ArtSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# class ArtList(generics.ListCreateAPIView):  
#     queryset = Art.objects.all()
#     serializer_class = ArtSerializer


class CreateArt(APIView):
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
        
