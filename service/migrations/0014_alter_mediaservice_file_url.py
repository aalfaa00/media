# Generated by Django 4.1.1 on 2022-10-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_rename_image_mediaservice_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaservice',
            name='file_url',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
