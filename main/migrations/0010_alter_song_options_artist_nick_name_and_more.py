# Generated by Django 4.2.7 on 2023-11-25 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_song_author_remove_song_composer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['title'], 'verbose_name': 'Песня', 'verbose_name_plural': 'Песни'},
        ),
        migrations.AddField(
            model_name='artist',
            name='nick_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Сценическое имя'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='song',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='author_songs', to='main.artist', verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='song',
            name='composers',
            field=models.ManyToManyField(blank=True, related_name='composer_songs', to='main.artist', verbose_name='Композиторы'),
        ),
        migrations.AlterField(
            model_name='song',
            name='performers',
            field=models.ManyToManyField(blank=True, related_name='performer_songs', to='main.artist', verbose_name='Исполнители'),
        ),
        migrations.DeleteModel(
            name='NickName',
        ),
    ]
