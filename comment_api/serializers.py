from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # description = serializers.JSONField()
    class Meta: 
        model = Comment
        fields = ('id','user', 'art', 'description', 'published')