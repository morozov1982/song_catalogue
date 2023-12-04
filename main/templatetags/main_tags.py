from django import template
from main.models import Song, Artist, Album, Genre


register = template.Library()


@register.simple_tag()
def get_genres():
    """Вывод всех стилей"""
    return Genre.objects.all()


@register.inclusion_tag('main/tags/last_songs.html')
def get_last_songs(count=5):
    songs = Song.objects.all()[:count]
    return {"last_songs": songs}
