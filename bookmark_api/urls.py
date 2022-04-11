from django.urls import path

from .views import BookmarkArt

app_name = 'bookmark_api'

urlpatterns = [
    path('bookmark/<int:art_id>', BookmarkArt.as_view(), name='bookmark')
]