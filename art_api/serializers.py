from rest_framework import serializers
from art.models import Art
from users.serializers import CustomUserSerializer

class ArtSerializer(serializers.ModelSerializer):
    # user = CustomUserSerializer(many=False)
    class Meta: 
        model = Art
        fields = ('id','title', 'image', 'genre', 'user', 'description', 'for_sale', 'status', 'price', 'likes')

