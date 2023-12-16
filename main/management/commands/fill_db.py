import os
import json
import re

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from slugify import slugify

from main.models import Song, Link, Artist


JSON_PATH = os.path.join('main', 'fixtures')


def replace_next_number(string):
    pattern = r'\d+$'
    match = re.search(pattern, string)
    if match:
        number = int(match.group())
        next_number = number + 1
        return re.sub(pattern, str(next_number), string)
    return string + '1'


def get_slug(obj_class, data):
    _slug = slugify(data).lower()
    _slug_obj = obj_class.objects.filter(slug=_slug)

    if _slug_obj:
        _slug = replace_next_number(_slug_obj.last().slug)

    return _slug


def get_or_create_artists(song_data, artist_type='performers'):
    artists = []

    if song_data.get(artist_type)[0]:
        for artist in song_data.get(artist_type):
            if not Artist.objects.filter(nick_name=artist).exists():
                _slug = get_slug(Artist, artist)

                _artist = Artist.objects.create(nick_name=artist, slug=_slug)
            else:
                _artist = Artist.objects.get(nick_name=artist)

            artists.append(_artist.pk)

    return artists


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name), mode='r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        songs = load_from_json('songs.json')

        for song_data in songs:
            _song = {
                'title': song_data.get('title'),
                'slug': get_slug(Song, song_data.get('title')),
                'key': song_data.get('key'),
                'chords': song_data.get('chords'),
                'bpm': float(song_data.get('bpm')) if song_data.get('bpm') else None,
                'additional': (f'<strong>Закольцованность припева:</strong> {song_data.get("chorus")}<br>'
                               f'<strong>Гармонии куплета и припева:</strong> <br>'
                               f'<strong>Диапазон: </strong> {song_data.get("range")}'),
            }

            _performers = get_or_create_artists(song_data, 'performers')
            _composers = get_or_create_artists(song_data, 'composers')
            _authors = get_or_create_artists(song_data, 'authors')

            _link_url = song_data.get('links')
            _link = Link.objects.filter(url=_link_url).first()

            if not _link:
                _link = Link.objects.create(url=_link_url, description='YouTube')

            new_song = Song.objects.create(**_song)

            new_song.performers.set(_performers)
            new_song.composers.set(_composers)
            new_song.authors.set(_authors)
            new_song.links.set([_link])

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', '', '123')
