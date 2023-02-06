from rest_framework import generics, permissions
from my_api.permissions import IsOwnerOrReadOnly
from saved.models import Saved
from saved.serializers import SavedSerializer


class SavedList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavedDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()
