from django.urls import path

from .views import SongListView, SongDetailView, ArtistDetailView, FilterSongsView, SearchView

app_name = 'main'

urlpatterns = [
    path('', SongListView.as_view(), name='index'),
    # path('<int:pk>/', SongDetailView.as_view(), name='song'),
    path('filter/', FilterSongsView.as_view(), name='filter'),
    path('search/', SearchView.as_view(), name='search'),
    path('<slug:slug>/', SongDetailView.as_view(), name='song'),
    path('artist/<slug:slug>/', ArtistDetailView.as_view(), name='artist'),
]
