from rest_framework import serializers
from feature.music.dataclass.music_request import MusicRequest


class CreateMusicRequest(serializers.Serializer):
    song_name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    singer = serializers.CharField(max_length=255)


    def validate(self, data):
        return MusicRequest(**data)
