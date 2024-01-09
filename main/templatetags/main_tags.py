from django import template
from main.models import Song, Artist, Album, Genre


register = template.Library()


@register.simple_tag()
def get_genres():
    """Вывод всех стилей"""
    return Genre.objects.all()


@register.filter()
def btn(description=None):
    """Замена надписей YouTube, VK на кнопки"""
    if description.lower() == 'youtube':
        return '<i class="bi bi-youtube fs-3"></i>'
    if description.lower() == 'vk':
        return '<i class="bi bi-play-circle-fill bi-vk fs-4"></i>'
    if description.lower() in ["ya", "yandex"]:
        return '<i class="bi bi-play-circle-fill bi-ya fs-4"></i>'
    return description


@register.inclusion_tag('main/tags/last_songs.html')
def get_last_songs(count=5):
    songs = Song.objects.order_by('-id')[:count]
    return {"last_songs": songs}


@register.inclusion_tag('main/tags/last_artists.html')
def get_last_artists(count=5):
    artists = Artist.objects.order_by('-id')[:count]
    return {"last_artists": artists}
