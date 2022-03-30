from rest_framework import serializers
from art.models import Art
from users.serializers import CustomUserSerializer

class ArtSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(many=False)
    class Meta: 
        model = Art
        fields = ('id','title', 'image', 'user', 'description', 'for_sale', 'status', 'price', 'likes')


# class VoteSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Vote
#         fields = ('user_id', 'art_id')