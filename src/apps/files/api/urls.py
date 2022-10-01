from django.urls import path, include, re_path
from rest_framework import routers
from .views import UploadViewSet, FileListView, FileDetailView


router = routers.DefaultRouter()
router.register('upload', UploadViewSet, basename='upload')

app_name = 'upload_files'

urlpatterns = [
    path('files/', FileListView.as_view(), name='files_list'),
    re_path(r'files/(?P<path>[^/]+)', FileListView.as_view(), name='files_path_list'),
    path('files/<pk>', FileDetailView.as_view(), name='files_detail'),
    path('', include(router.urls)),
]
