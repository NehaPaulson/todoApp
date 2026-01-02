from rest_framework import serializers


class GetOneMusicRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
