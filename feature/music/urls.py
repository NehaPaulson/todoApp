from django.urls import path
from feature.music.music_controller import MusicController

urlpatterns = [
    path("create/", MusicController.create),
    path("all/", MusicController.get_all),
    path("get/<int:id>/", MusicController.get_one),
    path("update/<int:id>/", MusicController.update),
    path("delete/<int:id>/", MusicController.delete),
]