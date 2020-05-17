from rest_framework import serializers
from galleryitem.models import GalleryItem

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = (
            'id',
            'product',
            'image',
            'created_at',
        )
