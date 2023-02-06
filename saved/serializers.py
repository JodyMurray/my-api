from django.db import IntegrityError
from rest_framework import serializers
from saved.models import Saved


class SavedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Saved
        fields = [
            'id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
