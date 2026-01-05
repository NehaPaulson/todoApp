from dataclasses import asdict

from feature.singer.model.models import Singer
from feature.common.common import Common
from feature.singer.serializer.response.singer_response import SingerResponse


class SingerView:

    @Common(
        response_handler=SingerResponse,
        message="Singer created successfully"
    ).exception_handler
    def create(self, params):
        return Singer.create(
            singer_name=params.singer_name,
            age=params.age,
            years_of_experience=params.years_of_experience
        )

    @Common(
        response_handler=SingerResponse,
        message="Data fetched successfully"
    ).exception_handler
    def get_all(self, request):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        queryset = Singer.get_all()
        return queryset[offset: offset + limit]

    @Common(
        response_handler=SingerResponse,
        message="Data fetched successfully"
    ).exception_handler
    def get_one(self, singer_id: int):
        singer = Singer.get_one(singer_id)
        if not singer:
            raise ValueError(f"id {singer_id} does not exist")
        return singer

    @Common(
        response_handler=SingerResponse,
        message="Singer updated successfully"
    ).exception_handler
    def update(self, singer_id: int, params):
        singer = Singer.get_one(singer_id)
        if not singer:
            raise ValueError(f"id {singer_id} does not exist")

        for key, value in asdict(params).items():
            if value is not None:
                setattr(singer, key, value)

        singer.save()
        return singer

    @Common(
        message="Singer deleted successfully"
    ).exception_handler
    def delete(self, singer_id: int):
        singer = Singer.get_one(singer_id)
        if not singer:
            raise ValueError(f"id {singer_id} does not exist")

        singer.delete()
        return {}
