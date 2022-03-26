

from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('', include('art.urls', namespace='arts')),
    # path('api/', include('art_api.urls', namespace='art_api')),
    path('token/', obtain_auth_token, name='token'),
    path('api/user/', include('users.urls', namespace='users')),
    path('api/art/', include('art_api.urls', namespace='art')),
    path('api/', include('bookmark_api.urls', namespace='bookmark'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)