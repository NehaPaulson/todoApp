from rest_framework import serializers
from feature.music.dataclass.music_request import MusicRequest


class CreateMusicRequest(serializers.Serializer):
    song_name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_null=True)
    singer = serializers.CharField(max_length=255)

    def save(self, **kwargs):
        return MusicRequest(
            song_name=self.validated_data.get("song_name"),
            description=self.validated_data.get("description"),
            singer=self.validated_data.get("singer"),
        )
