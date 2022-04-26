from django.urls import path
from .views import CustomUserCreate, FollowView, FollowedView, GetCurrentUser, ListAllArtistUser, ListAllUser, UploadProfilePicture, UserDetail, UserFilter

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('list_all_user/', ListAllUser.as_view(), name="list_all_user"),
    path('user_detail/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('list_all_artist_user/', ListAllArtistUser.as_view(), name="list_all_user"),
    path('follow_user/<int:user_id>', FollowView.as_view(), name="follow_user"),
    path('followed_user/<int:user_id>', FollowedView.as_view(), name="followed_user"),
    path('current_user/', GetCurrentUser.as_view(), name="current"),
    path('search/<str:user_name>/', UserFilter.as_view(), name="searchuser"),
    path('change_profile_picture/', UploadProfilePicture.as_view(), name="uploadprofilepicture"),
]