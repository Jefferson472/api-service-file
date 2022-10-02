from django.test import TestCase
from django.urls import reverse, resolve


class FileUrlTestCase(TestCase):
    def test_urls_upload(self):
        self.assertEqual(reverse('upload_files:upload-list'), '/api/upload/')
        self.assertEqual(resolve('/api/upload/').view_name, 'upload_files:upload-list')

    def test_urls_files(self):
        self.assertEqual(reverse('upload_files:files_list'), '/api/files/')
        self.assertEqual(resolve('/api/files/').view_name, 'upload_files:files_list')

    def test_urls_files_path(self):
        self.assertEqual(reverse('upload_files:files_path_list', kwargs={'path': 'home'}), '/api/files/home')
        self.assertEqual(resolve('/api/files/home').view_name, 'upload_files:files_path_list')

    def test_urls_file_detail(self):
        self.assertEqual(reverse('upload_files:file_detail', kwargs={'pk': 1}), '/api/file/1')
        self.assertEqual(resolve('/api/file/1').view_name, 'upload_files:file_detail')

    def test_urls_path_delete(self):
        self.assertEqual(reverse('upload_files:path_delete', kwargs={'path': 'home'}), '/api/path/home')
        self.assertEqual(resolve('/api/path/home').view_name, 'upload_files:path_delete')
