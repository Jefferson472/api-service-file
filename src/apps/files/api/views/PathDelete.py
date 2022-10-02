import os

from django.conf import settings
from django.http import HttpResponse

from rest_framework.decorators import api_view

from apps.files.models import File


@api_view(['DELETE', 'GET'])
def path_delete(request, **kwargs):
    if 'path' in kwargs:
        full_path = request.get_full_path()
        dir_path = full_path[full_path.rfind('/')+1:]
        file_dir = File.objects.filter(
            path=dir_path)
        if file_dir:
            response = f"The path {full_path} is not empty!"
            status_code = 400
        else:
            try:
                os.rmdir(os.path.join(settings.MEDIA_ROOT, 'home', str(full_path[10:])))
                response = f"Dir path {dir_path} was deleted"
                status_code = 200
            except Exception as e:
                response = e
                status_code = 400
        return HttpResponse(response, status=status_code)
