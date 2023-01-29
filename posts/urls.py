from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostsList.as_view()),
    path('posts/<int:pk>/', views.PostsDetail.as_view()),
]
