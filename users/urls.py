from django.urls import path
from .views import CustomUserCreate, ListAllArtistUser, ListAllUser, UserDetail

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('list_all_user/', ListAllUser.as_view(), name="list_all_user"),
    path('user_detail/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('list_all_artist_user/', ListAllArtistUser.as_view(), name="list_all_user"),
]