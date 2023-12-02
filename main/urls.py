from django.urls import path

from .views import SongListView, SongDetailView


app_name = 'main'

urlpatterns = [
    path('', SongListView.as_view(), name='index'),
    # path('<int:pk>/', SongDetailView.as_view(), name='song'),
    path('<slug:slug>/', SongDetailView.as_view(), name='song'),
]
