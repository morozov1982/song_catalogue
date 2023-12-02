from django.db.models import Min
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Song


# def index(request):
#     songs = Song.objects.annotate(first_performer_name=Min('performers__nick_name')).order_by(
#         'first_performer_name')
#     context = {'songs': songs}
#
#     return render(request, 'index.html', context)


class SongListView(ListView):
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


class SongDetailView(DetailView):
    """Полное описание песни"""
    model = Song
    # template_name = 'song/song_detail.html'
    # slug_field = 'slug'

    # def get(self, request, pk):
    #     song = Song.objects.get(id=pk)
    #     context = {'song': song}
    #
    #     return render(request, 'song_detail.html', context)
