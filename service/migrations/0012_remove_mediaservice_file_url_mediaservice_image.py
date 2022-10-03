# Generated by Django 4.1.1 on 2022-10-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_alter_mediaservice_file_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediaservice',
            name='file_url',
        ),
        migrations.AddField(
            model_name='mediaservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]