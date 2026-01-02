from rest_framework import serializers


class DeleteTodoRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
