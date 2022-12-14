# Generated by Django 4.1.1 on 2022-10-01 09:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file_url', models.FileField(upload_to='media/uploads')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned', models.BooleanField(default=False)),
            ],
        ),
    ]
