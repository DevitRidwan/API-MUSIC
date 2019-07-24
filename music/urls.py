from django.urls import path
from .views import MusicsView, MusicsDetail

urlpatterns = [
    path('musics', MusicsView.as_view(), name='musics'),
    path('musics/<int:pk>', MusicsDetail.as_view(), name='music-detail')
]