import os

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.status import HTTP_200_OK
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ..serializations import UploadSerializer
from apps.files.models import File


class FileDetail(RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = UploadSerializer

    def delete(self, request, *args, **kwargs):
        file_obj = get_object_or_404(File, pk=kwargs.get('pk'))
        os.remove(os.path.join(settings.MEDIA_ROOT, str(file_obj.file)))
        self.destroy(request, *args, **kwargs)
        response = f"File {file_obj.file_name} was deleted"
        return Response(response, status=HTTP_200_OK)

