from rest_framework import serializers


class DeleteMusicRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
