from django.urls import path

from follow_api.views import AllList, FollowUser, GetFollowerList, GetFollowingList, OtherFollowerList, OtherFollowingList

app_name = 'follow_api'

urlpatterns = [
    path('follow/<int:follower>', FollowUser.as_view(), name='follow_user'),
    path('list/', AllList.as_view(), name='all_list'),
    path('following/', GetFollowingList.as_view(), name='following_list'),
    path('follower/', GetFollowerList.as_view(), name='follower_list'),
    path('details_follower/<int:pk>/', OtherFollowerList.as_view(), name='detailfollownumber'),
    path('details_following/<int:pk>/', OtherFollowingList.as_view(), name='detailfollowingnumber'),
]