# Generated by Django 4.1.8 on 2023-09-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messengers', '0035_info_prof_pics_messages_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
