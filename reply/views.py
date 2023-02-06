from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from my_api.permissions import IsOwnerOrReadOnly
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer


class ReplyList(generics.ListCreateAPIView):

    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reply.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplyDetailSerializer
    queryset = Reply.objects.all()
