from django.urls import path

from api.views import (SongListAPIView, SongDetailAPIView, SongCreateAPIView,
                       ArtistListAPIView, ArtistDetailAPIView)

app_name = 'api'

urlpatterns = [
    path('songs/', SongListAPIView.as_view(), name='songs'),
    path('songs/<int:pk>/', SongDetailAPIView.as_view(), name='song'),
    path('songs/add/', SongCreateAPIView.as_view(), name='song_add'),

    path('artists/', ArtistListAPIView.as_view(), name='artists'),
    path('artists/<int:pk>/', ArtistDetailAPIView.as_view(), name='artist'),
]
