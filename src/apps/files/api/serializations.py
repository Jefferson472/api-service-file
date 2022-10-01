from rest_framework import serializers

from ..models import File


class UploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    
    class Meta:
        model = File
        fields = ["file"]
