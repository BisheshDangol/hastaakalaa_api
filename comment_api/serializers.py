from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # description = serializers.JSONField()
    # user = serializers.StringRelatedField()
    # art = serializers.StringRelatedField()
    # user_email= serializers.ReadOnlyField(source='newuser.email')
    class Meta: 
        model = Comment
        fields = ('id','user', 'art', 'description', 'published')