from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    user = models.ForeignKey(
        User, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='home')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_files'
        ordering = ['-updated']
