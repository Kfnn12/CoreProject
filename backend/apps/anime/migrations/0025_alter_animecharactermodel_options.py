# Generated by Django 4.0.4 on 2022-05-09 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0024_animeinfomodel_anime_characters"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="animecharactermodel",
            options={"verbose_name": "Anime Character"},
        ),
    ]