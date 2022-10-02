from django.db import models
from django.contrib.auth.models import User


def get_path(instance, filename):
    path = instance.path
    if path == 'home' or path == '':        
        return f'{instance.user}/home/{filename}'
    else:
        return f'{instance.user}/home/{path}/{filename}'


class File(models.Model):
    user = models.ForeignKey(
        User, related_name='files', on_delete=models.CASCADE)
    path = models.CharField(default='', max_length=100)
    file = models.FileField(upload_to=get_path)
    file_name = models.CharField(
        default=file.name, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_files'
        ordering = ['-updated']

    def __str__(self):
        return self.file_name
