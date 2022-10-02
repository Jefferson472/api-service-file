import os
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase


class FileTestViews(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user", password="123456"
        )

        self.client.login(username='test_user', password='123456')
        self.client.force_authenticate(user=self.user)

    def test_file_upload(self):
        file_up = SimpleUploadedFile(
            'simple_file.pdf',
            b"file_content",
            content_type="application/pdf"
        )
        res = self.client.post(
            '/api/upload/',
            {
                'file': file_up,
                'path': 'test-dir'
            },
        )
        self.assertEqual(res.status_code, 201)

        res = self.client.get('/api/files/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)

        res = self.client.post(
            '/api/upload/',
            {
                'file': file_up,
                'path': 'test-dir'
            },
        )
        self.assertEqual(res.status_code, 200)

        res = self.client.delete('/api/file/1')
        self.assertEqual(res.status_code, 200)


    def test_file_ext_not_allowed(self):
        file_up = SimpleUploadedFile(
            os.path.join(settings.BASE_DIR.parent, 'README.md'),
            b"file_content",
            content_type="text/x-markdown"
        ) 
        res = self.client.post(
            '/api/upload/',
            {
                'file': file_up,
                'path': 'test-dir'
            },
        )
        self.assertEqual(res.status_code, 401)
        self.client.delete('/api/file/1')
