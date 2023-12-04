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


class GenreYear:
    """Жанры и годы выхода песен"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Song.objects.filter(year__isnull=False).order_by('year').values("year")


class SongListView(GenreYear, ListView):
    """Список песен"""
    model = Song
    queryset = Song.objects.annotate(first_performer_name=Min('performers__nick_name')).order_by(
        'first_performer_name')
    # template_name = 'index.html'

    # def get(self, request):
    #     songs = Song.objects.annotate(first_performer_name=Min('performers__nick_name')).order_by(
    #         'first_performer_name')
    #     context = {'songs': songs}
    #
    #     return render(request, 'index.html', context)


class SongDetailView(GenreYear, DetailView):
    """Полное описание песни"""
    model = Song
    # template_name = 'song/song_detail.html'
    # slug_field = 'slug'

    # def get(self, request, pk):
    #     song = Song.objects.get(id=pk)
    #     context = {'song': song}
    #
    #     return render(request, 'song_detail.html', context)


class ArtistDetailView(DetailView):
    """Вывод информации об артисте"""
    model = Artist


class FilterSongsView(GenreYear, ListView):
    """Фильтр песен"""
    def get_queryset(self):
        queryset = Song.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset


class SearchView(ListView):
    """Поиск песен и артистов"""

    def get_queryset(self):
        queryset = Song.objects.filter(
            Q(title__icontains=self.request.GET.get("q")) |
            Q(performers__nick_name__icontains=self.request.GET.get("q"))
        )
        return queryset
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=None, **kwargs)
    #     context['q'] = self.request.GET.get('q')
    #     return context
