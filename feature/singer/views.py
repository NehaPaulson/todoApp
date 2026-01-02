from dataclasses import asdict
from rest_framework.response import Response
from rest_framework import status

from feature.singer.model.models import Singer
from feature.singer.serializer.response.singer_response import SingerResponse
from feature.common.utils import Utils


class SingerView:

    def create(self, params):
        singer = Singer.create(
            singer_name=params.singer_name,
            age=params.age,
            years_of_experience=params.years_of_experience
        )
        data = SingerResponse(singer).data
        return Response(
            Utils.success_response("Singer created successfully", data),
            status=status.HTTP_201_CREATED
        )

    def get_all(self, request):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        queryset = Singer.get_all()
        total = queryset.count()

        singers = queryset[offset: offset + limit]
        data = SingerResponse(singers, many=True).data

        return Response(
            Utils.paginated_response(
                data=data,
                total=total,
                limit=limit,
                offset=offset,
                message="Data fetched successfully"
            )
        )

    def get_one(self, singer_id):
        singer = Singer.get_one(singer_id)
        if not singer:
            return Response(
                Utils.error_response("Singer not found", f"id {singer_id} does not exist"),
                status=404
            )
        data = SingerResponse(singer).data
        return Response(Utils.success_response("Data fetched successfully", data))

    def update(self, singer_id, params):
        singer = Singer.update(
            singer_id,
            singer_name=params.singer_name,
            age=params.age,
            years_of_experience=params.years_of_experience
        )
        if not singer:
            return Response(
                Utils.error_response("Singer not found", f"id {singer_id} does not exist"),
                status=404
            )
        data = SingerResponse(singer).data
        return Response(Utils.success_response("Singer updated successfully", data))

    def delete(self, singer_id):
        success = Singer.delete_one(singer_id)
        if not success:
            return Response(
                Utils.error_response("Singer not found", f"id {singer_id} does not exist"),
                status=404
            )
        return Response(Utils.success_response("Singer deleted successfully"))
