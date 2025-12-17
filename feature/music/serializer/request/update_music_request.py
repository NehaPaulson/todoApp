from rest_framework import serializers
from feature.music.dataclass.music_request import MusicRequest


class UpdateMusicRequest(serializers.Serializer):
    song_name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    singer = serializers.CharField(max_length=255, required=False)


    def validate(self, data):
        return MusicRequest(**data)
