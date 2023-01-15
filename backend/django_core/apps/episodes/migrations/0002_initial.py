# Generated by Django 4.2 on 2023-01-15 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("episodes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="episodetimestampmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="episodemodel",
            name="episode_comments",
            field=models.ManyToManyField(blank=True, to="episodes.episodecommentmodel"),
        ),
        migrations.AddField(
            model_name="episodemodel",
            name="episode_timestamps",
            field=models.ManyToManyField(blank=True, to="episodes.episodetimestampmodel"),
        ),
        migrations.AddField(
            model_name="episodecommentmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]