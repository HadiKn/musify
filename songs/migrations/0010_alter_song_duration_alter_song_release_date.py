# Generated by Django 5.2 on 2025-05-19 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0009_alter_song_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=datetime.date(2025, 5, 19)),
        ),
    ]
