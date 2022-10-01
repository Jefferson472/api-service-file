from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    user = models.ForeignKey(
        User, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='home')
    file_name = models.CharField(
        default=file.name, max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_files'
        ordering = ['-updated']

    def __str__(self):
        return self.file_name
