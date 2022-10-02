import os
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APITestCase

from apps.files.models import File


class FileModelTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user", password="123456")
        file_up = SimpleUploadedFile(
            'simple_file.pdf',
            b"simple_content",
            content_type="application/pdf"
        ) 
        File.objects.create(
            user=self.user,
            file_name=str(file_up.name).replace(' ', '_'),
            file=file_up,
        )
        self.file = File.objects.get(pk=1)

        self.client.login(username='test_user', password='123456')
        self.client.force_authenticate(user=self.user)

        res = self.client.delete('/api/file/1')
        self.assertEqual(res.status_code, 200)
    
    def test_name(self):
        self.assertEqual(self.file.file_name, 'simple_file.pdf')


    def test_path(self):
        self.assertEqual(self.file.path, '')
