from django.urls import path 
from .views import CreateArt

app_name = 'art_api'

urlpatterns = [
    # This is going to take in primary key  
    # This view is used to show the details of the blog which match the blog number.
    # Individual post
    # path('<int:pk>/', ArtDetail.as_view(), name='detailcreate'),

    # This view is used to show all the data in the database.
    # All post
    path('create_art/', CreateArt.as_view(), name='createart'),
]