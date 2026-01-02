from rest_framework import serializers


class GetAllTodoRequestSerializer(serializers.Serializer):
    limit = serializers.IntegerField(required=False, min_value=1)
    offset = serializers.IntegerField(required=False, min_value=0)
