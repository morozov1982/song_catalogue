from django.urls import path

from .views import SongListView, SongDetailView, ArtistDetailView, FilterSongsView

app_name = 'main'

urlpatterns = [
    path('', SongListView.as_view(), name='index'),
    # path('<int:pk>/', SongDetailView.as_view(), name='song'),
    path('filter/', FilterSongsView.as_view(), name='filter'),
    path('<slug:slug>/', SongDetailView.as_view(), name='song'),
    path('artist/<slug:slug>/', ArtistDetailView.as_view(), name='artist'),
]
