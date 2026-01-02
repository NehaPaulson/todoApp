from rest_framework import serializers


class MusicResponse(serializers.Serializer):
    id = serializers.IntegerField()
    song_name = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    singer = serializers.CharField(source="singer.singer_name")  # ✅ FK-safe
    created_at = serializers.DateTimeField()
