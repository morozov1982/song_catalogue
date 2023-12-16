from django.urls import path

from api.views import SongListAPIView, SongDetailAPIView, SongCreateAPIView

app_name = 'api'

urlpatterns = [
    path('songs/', SongListAPIView.as_view(), name='songs'),
    path('song/<int:pk>/', SongDetailAPIView.as_view(), name='song'),
    path('song/add/', SongCreateAPIView.as_view(), name='song_add'),
]
