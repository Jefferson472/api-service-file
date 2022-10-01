from django.urls import path, include, re_path
from rest_framework import routers
from .views import UploadViewSet, FileUploadView


router = routers.DefaultRouter()

app_name = 'upload_files'

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
]
