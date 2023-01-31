from django.urls import path
from reply import views

urlpatterns = [
    path('reply/', views.ReplyList.as_view()),
    path('reply/<int:pk>/', views.ReplyDetail.as_view())
]
