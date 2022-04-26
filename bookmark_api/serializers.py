from rest_framework import serializers
from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # art = serializers.StringRelatedField()
    class Meta: 
        model = Bookmark
        fields = ('id','user', 'art')