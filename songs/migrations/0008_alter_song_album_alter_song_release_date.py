# Generated by Django 5.2 on 2025-05-17 17:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_alter_album_release_date'),
        ('songs', '0007_alter_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=datetime.date(2025, 5, 17)),
        ),
    ]
