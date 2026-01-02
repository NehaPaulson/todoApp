from rest_framework import serializers
from feature.singer.dataclass.singer_request import SingerRequest


class CreateSingerRequestSerializer(serializers.Serializer):
    singer_name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(min_value=0)
    years_of_experience = serializers.IntegerField(min_value=0)

    def save(self, **kwargs):
        return SingerRequest(**self.validated_data)
