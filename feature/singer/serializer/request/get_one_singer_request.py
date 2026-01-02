from rest_framework import serializers


class GetOneSingerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
