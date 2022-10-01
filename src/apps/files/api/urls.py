from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet, FileListView, FileDetailView


router = routers.DefaultRouter()
router.register('upload', UploadViewSet)

app_name = 'upload_files'

urlpatterns = [
    path('files/', FileListView.as_view(), name='files_list'),
    path('files/<pk>', FileDetailView.as_view(), name='files_detail'),
    path('', include(router.urls)),
]
