# Generated by Django 4.1.1 on 2022-10-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="file_name",
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
    ]
