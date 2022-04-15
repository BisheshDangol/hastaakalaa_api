from django.urls import path

from .views import CommentArt, GetCommentByPost

app_name = 'comment_api'

urlpatterns = [
    path('comment/<int:art_id>', CommentArt.as_view(), name='comment'),
    path('get/comments/<int:art_id>', GetCommentByPost.as_view(), name='getcomment')
]