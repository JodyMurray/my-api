from django.urls import path
from downvotes import views

urlpatterns = [
    path('downvotes/', views.DownVoteList.as_view()),
    path('downvotes/<int:pk>/', views.DownVoteDetail.as_view()),
]
