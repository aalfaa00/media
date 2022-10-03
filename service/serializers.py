from rest_framework import serializers
from .models import MediaService
from django.conf import settings

class MediaServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaService
        fields = ['id', 'file_url', 'created_at', 'assigned']
        
    def get_photo_url(self, mediaservice):
        request = self.context.get('request')
        photo_url = mediaservice.file_url.url
        return request.build_absolute_uri(photo_url)

