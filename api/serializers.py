from rest_framework import serializers

from main.models import Song, Artist


class ArtistListSerializer(serializers.ModelSerializer):
    """Список артистов"""

    class Meta:
        model = Artist
        fields = ('id', 'nick_name')


class ArtistDetailSerializer(serializers.ModelSerializer):
    """Подробная информация об артисте"""

    class Meta:
        model = Artist
        fields = '__all__'


class SongListSerializer(serializers.ModelSerializer):
    """Список песен"""

    performers = ArtistListSerializer(read_only=True, many=True,)

    genres = serializers.SlugRelatedField(
        slug_field='name', read_only=True, many=True,
    )

    class Meta:
        model = Song
        fields = ('id', 'title', 'performers', 'year', 'genres')


class SongDetailSerializer(serializers.ModelSerializer):
    """Подробная информация о песне"""

    performers = serializers.SlugRelatedField(
        slug_field='nick_name', read_only=True, many=True,
    )

    composers = serializers.SlugRelatedField(
        slug_field='nick_name', read_only=True, many=True,
    )

    authors = serializers.SlugRelatedField(
        slug_field='nick_name', read_only=True, many=True,
    )

    genres = serializers.SlugRelatedField(
        slug_field='name', read_only=True, many=True,
    )

    class Meta:
        model = Song
        fields = '__all__'


class SongCreateSerializer(serializers.ModelSerializer):
    """Добавление песни"""

    class Meta:
        model = Song
        fields = '__all__'
