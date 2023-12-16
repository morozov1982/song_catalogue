from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Стили"""
    name = models.CharField(verbose_name='Стиль', max_length=100)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    slug = models.SlugField(max_length=130, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'
        ordering = ['name']


class Song(models.Model):
    """Песни"""
    title = models.CharField(verbose_name='Название', max_length=120)
    bpm = models.FloatField(verbose_name='Темп', blank=True, null=True)
    key = models.CharField(verbose_name='Тональность', max_length=16, blank=True, null=True)
    performers = models.ManyToManyField('Artist', related_name='performer_songs', verbose_name='Исполнители',
                                        blank=True)
    composers = models.ManyToManyField('Artist', related_name='composer_songs', verbose_name='Композиторы', blank=True)
    authors = models.ManyToManyField('Artist', related_name='author_songs', verbose_name='Авторы', blank=True)
    lyrics = models.TextField(verbose_name='Слова', blank=True, null=True)
    chords = models.CharField(verbose_name='Аккорды', max_length=255, blank=True, null=True)
    year = models.PositiveSmallIntegerField('Год релиза', blank=True, null=True)
    cover_image = models.ImageField('Обложка', upload_to='song_covers/', blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='genre_songs', verbose_name='Стили', blank=True)
    additional = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True,
                                  default='<strong>Закольцованность припева:</strong> <br>'
                                          '<strong>Гармонии куплета и припева:</strong> <br>'
                                          '<strong>Диапазон:</strong>')
    slug = models.SlugField(max_length=130, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:song', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class Link(models.Model):
    """Ссылки"""
    url = models.URLField('Ссылка')
    description = models.CharField(verbose_name='Описание', max_length=255, blank=True, null=True)
    songs = models.ForeignKey('Song', verbose_name='Песня', related_name='links', on_delete=models.CASCADE, blank=True,
                              null=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Album(models.Model):
    """Альбомы"""
    title = models.CharField(verbose_name='Название', max_length=120)
    artist = models.ManyToManyField('Artist', verbose_name='Исполнители', related_name='albums')
    release_date = models.DateField('Дата релиза', blank=True, null=True)
    cover_image = models.ImageField('Обложка', upload_to='album_covers/', blank=True, null=True)
    songs = models.ManyToManyField('Song', related_name='albums', verbose_name='Песни', blank=True)
    slug = models.SlugField(max_length=130, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class ArtistImage(models.Model):
    """Изображения артиста"""
    image = models.ImageField('Изображения', upload_to='artist_images/', blank=True, null=True)
    description = models.CharField(verbose_name='Описание', max_length=255, blank=True, null=True)
    artist = models.ForeignKey('Artist', verbose_name='Артист', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Artist(models.Model):
    """Артист"""
    nick_name = models.CharField(verbose_name='Сценическое имя', max_length=255)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True, null=True)
    sur_name = models.CharField(verbose_name='Отчество', max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True, null=True)
    bio = models.TextField(verbose_name='Биография', blank=True, null=True)
    slug = models.SlugField(max_length=130, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.nick_name

    def get_absolute_url(self):
        return reverse('main:artist', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'
        ordering = ['nick_name']
