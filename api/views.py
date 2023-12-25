from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from main.models import Song, Artist
from .serializers import (SongListSerializer, SongCreateSerializer, SongDetailSerializer,
                          ArtistDetailSerializer, ArtistListSerializer)


class SongListAPIView(ListAPIView):
    """Вывод списка песен"""

    queryset = Song.objects.all()
    serializer_class = SongListSerializer


class SongDetailAPIView(RetrieveAPIView):
    """Подробная информация о песне"""

    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer


class SongCreateAPIView(CreateAPIView):
    """Добавление песни"""

    serializer_class = SongCreateSerializer


class ArtistListAPIView(ListAPIView):
    """Вывод списка артистов"""
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer


class ArtistDetailAPIView(RetrieveAPIView):
    """Подробная информация об артисте"""
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer

