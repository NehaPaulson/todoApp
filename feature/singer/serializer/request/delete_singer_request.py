from rest_framework import serializers


class DeleteSingerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
