from rest_framework import serializers
from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Map the image model instance into JSON format."""

   # created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        """Map serializer fields to image model fields."""
        model = Image
        fields = "__all__"

class ImageSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ["created_by", "meetup_id"]