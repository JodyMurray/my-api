from rest_framework import generics, permissions
from my_api.permissions import IsOwnerOrReadOnly
from downvotes.models import DownVote
from downvotes.serializers import DownVoteSerializer


class DownVoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DownVoteSerializer
    queryset = DownVote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DownVoteDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DownVoteSerializer
    queryset = DownVote.objects.all()
