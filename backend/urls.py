from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  
    path('api/songs/', include('songs.urls')),
    path('api/albums/', include('albums.urls')),
    path('api/playlists/', include('playlists.urls')),
    path('api/follows/', include('follows.urls')),

]


if settings.DEBUG : 
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


