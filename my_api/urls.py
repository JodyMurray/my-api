from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('reply.urls')),
    path('', include('votes.urls')),
    path('', include('downvotes.urls')),
    path('', include('followers.urls')),
    path('', include('saved.urls')),
]
