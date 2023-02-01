from django.db.models import Count
from rest_framework import generics, permissions, filters
from my_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostsList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        downvotes_count=Count('downvotes', distinct=True),
        reply_count=Count('replies', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'votes_count',
        'downvotes_count',
        'reply_count',
        'votes__created_at',
        'downvotes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        votes_count=Count('votes', distinct=True),
        downvotes_count=Count('downvotes', distinct=True),
        reply_count=Count('replies', distinct=True),
    ).order_by('-created_at')
