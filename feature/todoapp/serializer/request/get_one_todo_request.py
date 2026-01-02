from rest_framework import serializers


class GetOneTodoRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
