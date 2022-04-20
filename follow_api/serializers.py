from follow.models import Follow
from rest_framework import serializers


class FollowSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Follow
        fields = ('id','user_id', 'follower_id')