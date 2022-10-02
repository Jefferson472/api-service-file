import os

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.status import HTTP_200_OK
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ..serializations import UploadSerializer
from apps.files.models import File


class FileDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UploadSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        file_obj = get_object_or_404(
            File, pk=kwargs.get('pk'), user=request.user
        )

        if file_obj.path == '':
            path = 'home'
        else:
            path = f'home/{file_obj.path}'

        os.remove(os.path.join(
            settings.MEDIA_ROOT,
            str(request.user),
            path,
            str(file_obj.file_name).replace(' ', '_'),
        ))
        self.destroy(request, *args, **kwargs)
        response = f"File {file_obj.file_name} was deleted"
        return Response(response, status=HTTP_200_OK)

