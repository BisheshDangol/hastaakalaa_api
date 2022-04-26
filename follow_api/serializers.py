from follow.models import Follow
from rest_framework import serializers


class FollowSerializer(serializers.ModelSerializer):
    # user_id = serializers.StringRelatedField()
    # follower_id = serializers.StringRelatedField()
    class Meta: 
        model = Follow
        fields = ('id','user_id', 'follower_id')