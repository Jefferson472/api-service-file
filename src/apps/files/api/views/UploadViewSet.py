import os
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.response import Response

from ..serializations import UploadSerializer
from ...models import File


class UploadViewSet(viewsets.ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):
        up_file = request.data['file']
        path = request.data.get('path')

        try:
            obj = File.objects.get(file_name=up_file.name, path=path)
            os.remove(os.path.join(settings.MEDIA_ROOT, str(obj.file)))
            obj.file = up_file
            obj.save()
            response = f"File {up_file} updated!"
            status_code = status.HTTP_200_OK
        except Exception:
            File.objects.create(
                user=request.user,
                path=path,
                file_name=up_file.name,
                file=up_file,
            ).save()
            response = f"POST API and you have uploaded a {up_file} file"
            status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)
