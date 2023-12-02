# Generated by Django 4.2.7 on 2023-11-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_song_options_alter_song_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='author_order',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Порядок авторов'),
        ),
        migrations.AddField(
            model_name='song',
            name='composer_order',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Порядок композиторов'),
        ),
        migrations.AddField(
            model_name='song',
            name='performer_order',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Порядок исполнителей'),
        ),
    ]
