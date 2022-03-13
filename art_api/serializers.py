from rest_framework import serializers
from art.models import Art

class ArtSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Art
        fields = ('id','title', 'image', 'user', 'description', 'for_sale', 'status', 'price')


# class VoteSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Vote
#         fields = ('user_id', 'art_id')