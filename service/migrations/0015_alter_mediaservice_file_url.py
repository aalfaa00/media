# Generated by Django 4.1.1 on 2022-10-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_alter_mediaservice_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaservice',
            name='file_url',
            field=models.FileField(default=None, upload_to='uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
