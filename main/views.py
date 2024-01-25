from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Min, Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Song, Artist, Genre


# def index(request):
#     songs = Song.objects.annotate(first_performer_name=Min('performers__nick_name')).order_by(
#         'first_performer_name')
#     context = {'songs': songs}
#
#     return render(request, 'index.html', context)


class DataMixin:
    paginate_by = 20


class GenreYear:
    """Жанры и годы выхода песен"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Song.objects.filter(year__isnull=False).distinct().order_by('year').values("year")


class SongListView(DataMixin, GenreYear, ListView):
    """Список песен"""
    model = Song

    def get_queryset(self):
        return Song.objects.annotate(first_performer_name=Min('performers__nick_name')).order_by(
            'first_performer_name')


class SongDetailView(GenreYear, DetailView):
    """Полное описание песни"""
    model = Song


class ArtistListView(DataMixin, GenreYear, ListView):
    """Список артистов"""
    model = Artist


class ArtistDetailView(DetailView):
    """Вывод информации об артисте"""
    model = Artist


class FilterSongsView(GenreYear, ListView):
    """Фильтр песен"""
    def get_queryset(self):
        queryset = Song.objects.all()

        years = self.request.GET.getlist("year")
        genres = self.request.GET.getlist("genre")

        if years:
            queryset = queryset.filter(year__in=years)
        if genres:
            queryset = queryset.filter(genres__name__in=genres)

        return queryset


class SearchView(ListView):
    """Поиск песен и артистов"""

    def get_queryset(self):
        queryset = Song.objects.filter(
            Q(title__icontains=self.request.GET.get("q")) |
            Q(performers__nick_name__icontains=self.request.GET.get("q"))
        ).distinct()
        return queryset
