from django.urls import path, include, re_path
from rest_framework import routers

from .views.FileListView import FileListView
from .views.UploadViewSet import UploadViewSet
from .views.FileDetail import FileDetail
from .views.PathDelete import path_delete


router = routers.DefaultRouter()
router.register('upload', UploadViewSet, basename='upload')

app_name = 'upload_files'

urlpatterns = [
    path('files/', FileListView.as_view(), name='files_list'),
    re_path(r'files/(?P<path>[^/]+)', FileListView.as_view(), name='files_path_list'),
    path('file/<int:pk>', FileDetail.as_view(), name='file_detail'),
    re_path(r'path/(?P<path>[^/]+)', path_delete, name='path_delete'),
    path('', include(router.urls)),
]
