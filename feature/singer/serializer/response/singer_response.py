from rest_framework import serializers


class SingerResponse(serializers.Serializer):
    id = serializers.IntegerField()
    singer_name = serializers.CharField()
    age = serializers.IntegerField()
    years_of_experience = serializers.IntegerField()
