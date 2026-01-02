from rest_framework import serializers
from feature.singer.dataclass.singer_request import SingerRequest


class UpdateSingerRequestSerializer(serializers.Serializer):
    singer_name = serializers.CharField(max_length=255, required=False)
    age = serializers.IntegerField(min_value=0, required=False)
    years_of_experience = serializers.IntegerField(min_value=0, required=False)

    def save(self, **kwargs):
        return SingerRequest(**self.validated_data)
