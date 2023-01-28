from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostsList.as_view()),
]
