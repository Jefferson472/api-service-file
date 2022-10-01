import os
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.conf import settings

from .serializations import UploadSerializer
from ..models import File


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = UploadSerializer

class FileDetailView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = UploadSerializer


class UploadViewSet(viewsets.ViewSet):
    queryset = File.objects.all()
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
            response = "POST API and you have uploaded a {} file".format(up_file)
            status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)
