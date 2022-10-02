import os
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.files.models import File


class FileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user", password="123456")
        doc_file = os.path.join(
            settings.BASE_DIR.parent, 'docs\Simple File Service brief.pdf')
        file_up = SimpleUploadedFile(
            doc_file, b"file_content", content_type="application/pdf") 
        self.file = File.objects.create(
            user=self.user, file_name=file_up.name, file=doc_file)
    
    def test_name(self):
        self.assertEqual(self.file.file_name, 'Simple File Service brief.pdf')

    def test_path(self):
        self.assertEqual(self.file.path, 'home')
