# Generated by Django 4.1.7 on 2023-04-06 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messengers', '0008_friends_sent_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 6, 13, 6, 10, 740336)),
        ),
    ]
