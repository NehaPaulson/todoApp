from django.db import models
from feature.singer.model.models import Singer


class Music(models.Model):
    song_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name="songs",
        db_column="singer"   
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"


    @staticmethod
    def create(song_name: str, description: str = "", singer: Singer = None):
        return Music.objects.create(
            song_name=song_name,
            description=description,
            singer=singer
        )

    @staticmethod
    def update(
        music_id: int,
        song_name: str = None,
        description: str = None,
        singer: Singer = None
    ):
        music = Music.objects.filter(id=music_id).first()
        if not music:
            return None

        if song_name is not None:
            music.song_name = song_name

        if description is not None:
            music.description = description

        if singer is not None:
            music.singer = singer

        music.save()
        return music
