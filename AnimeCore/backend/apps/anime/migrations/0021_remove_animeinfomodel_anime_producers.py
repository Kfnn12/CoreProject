# Generated by Django 4.0.3 on 2022-03-28 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0020_remove_animeinfomodel_anime_studios"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animeinfomodel",
            name="anime_producers",
        ),
    ]
