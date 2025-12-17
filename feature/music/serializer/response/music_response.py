from rest_framework import serializers


class MusicResponse(serializers.Serializer):
    id = serializers.IntegerField()
    song_name = serializers.CharField()
    description = serializers.CharField()
    singer = serializers.CharField()
    created_at = serializers.DateTimeField()
