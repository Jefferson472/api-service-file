# Generated by Django 4.1.1 on 2022-10-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0002_file_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="path",
            field=models.CharField(default="home", max_length=100),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(
                upload_to=models.CharField(default="home", max_length=100)
            ),
        ),
    ]
