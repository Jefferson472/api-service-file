import os, mimetypes
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from ..serializations import UploadSerializer
from ...models import File


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = UploadSerializer

    def list(self, request, **kwargs):
        if 'path' in kwargs:
            full_path = request.get_full_path()
            format_list = ['.pdf', '.xml', '.txt']
            if full_path[-4:] in format_list:
                file_obj = get_object_or_404(
                    File,
                    file_name=full_path[full_path.rfind('/')+1:],
                    path=full_path[11:full_path.rfind('/')],
                )

                media_file = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))

                mimetype = mimetypes.guess_type(media_file)
                response = HttpResponse(open(media_file, 'rb'), status=200)
                response['Content-Disposition'] = f'attachment; filename={file_obj.file_name}'
                response['Content-Type'] = mimetype
                return response
            else:
                queryset = File.objects.filter(path__contains=full_path[11:-1])
                serializer = UploadSerializer(queryset, many=True)
                response = serializer.data
            return Response(response, status.HTTP_200_OK)
        
        return super().list(request, **kwargs)
