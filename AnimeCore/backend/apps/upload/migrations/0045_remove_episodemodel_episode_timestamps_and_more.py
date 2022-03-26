# Generated by Django 4.0.3 on 2022-03-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0044_alter_episodetimestampmodel_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="episodemodel",
            name="episode_timestamps",
        ),
        migrations.AddField(
            model_name="episodemodel",
            name="episode_timestamps",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="upload.episodetimestampmodel",
            ),
        ),
    ]
