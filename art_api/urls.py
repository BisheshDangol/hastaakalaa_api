from django.urls import path 
from .views import AbstractGenreArtFilter, ArtDetail, ArtDetails, BookmarkArt, CreateArt, LikeView, ListUserArtPost, PostListDetailFilter, RetrieveAllArtPost

app_name = 'art_api'

urlpatterns = [
    # This is going to take in primary key  
    # This view is used to show the details of the blog which match the blog number.
    # Individual post
    # path('<int:pk>/', ArtDetail.as_view(), name='detailcreate'),

    # This view is used to show all the data in the database.
    # All post
    path('create_art/', CreateArt.as_view(), name='createart'),
    path('detail_art/<str:pk>/', ArtDetail.as_view(), name='detailart'),
    path('details_art/<int:pk>/', ArtDetails.as_view(), name='detailnumberart'),
    path('search/custom/', PostListDetailFilter.as_view(), name='searchart'),
    path('get_all_art_post_user/', ListUserArtPost.as_view(), name='listuserartposts'),
    path('retrieve_art_post/', RetrieveAllArtPost.as_view(), name='retrieveartpost'),
    path('likes/<int:art_id>/change/', LikeView.as_view(), name='likeposts'),
    path('genre/<str:genre>', AbstractGenreArtFilter.as_view(), name='filterabstract'),
    path('bookmark/<int:art_id>/', BookmarkArt.as_view(), name='filterabstract'),
    
]