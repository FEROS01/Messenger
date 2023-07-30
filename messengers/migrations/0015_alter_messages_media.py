# Generated by Django 4.1.7 on 2023-07-25 12:55

import django.core.validators
from django.db import migrations
import messengers.models


class Migration(migrations.Migration):

    dependencies = [
        ('messengers', '0014_alter_info_prof_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='media',
            field=messengers.models.models.FileField(blank=True, null=True, upload_to=messengers.models.user_directory_media, validators=[django.core.validators.FileExtensionValidator(
                ['gif', 'png', 'jpeg', 'jpg', 'webp', 'avif', 'apng', 'mp4', 'webm', 'ogv', 'pdf', 'txt', 'csv', 'json', 'mp3', 'wav', 'oga'], 'Unsupported File format'), messengers.models.file_size_val, messengers.models.file_type_validator]),
        ),
    ]
