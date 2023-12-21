from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.models import Song, Artist
from .serializers import (SongListSerializer, SongCreateSerializer, SongDetailSerializer,
                          ArtistDetailSerializer, ArtistListSerializer)


class SongListAPIView(APIView):
    """Вывод списка песен"""
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongListSerializer(songs, many=True)
        return Response(serializer.data)


class SongDetailAPIView(APIView):
    """Подробная информация о песне"""
    def get(self, request, pk):
        song = Song.objects.get(id=pk)
        serializer = SongDetailSerializer(song)
        return Response(serializer.data)


class SongCreateAPIView(APIView):
    """Добавление песни"""
    def post(self, request):
        song = SongCreateSerializer(data=request.data)
        if song.is_valid():
            song.save()
        return Response(status=201)


class ArtistListAPIView(ListAPIView):
    """Вывод списка артистов"""
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer


class ArtistDetailAPIView(RetrieveAPIView):
    """Подробная информация об артисте"""
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer

