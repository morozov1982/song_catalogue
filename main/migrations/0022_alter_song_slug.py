# Generated by Django 4.2.7 on 2023-11-30 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(max_length=130, unique=True, verbose_name='Слаг'),
        ),
    ]
