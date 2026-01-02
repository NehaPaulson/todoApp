from dataclasses import asdict
from rest_framework.response import Response
from rest_framework import status

from feature.music.model.models import Music
from feature.music.serializer.response.music_response import MusicResponse
from feature.common.utils import Utils
from feature.singer.model.models import Singer


class MusicView:

    @staticmethod
    def create(data):
        singer = Singer.get_by_name(data.singer)
        if not singer:
            return Response(
                Utils.error_response(
                    "Singer not found",
                    f"singer_name '{data.singer}' does not exist"
                ),
                status=status.HTTP_404_NOT_FOUND
            )

        music = Music.objects.create(
            song_name=data.song_name,
            description=data.description,
            singer=singer,   # ✅ FK object
        )

        data = MusicResponse(music).data
        return Response(
            Utils.success_response("Music created successfully", data),
            status=status.HTTP_201_CREATED
        )

    @staticmethod
    def get_all(request):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        queryset = Music.objects.all()
        total = queryset.count()

        musics = queryset[offset: offset + limit]
        data = MusicResponse(musics, many=True).data

        return Response(
            Utils.paginated_response(
                data=data,
                total=total,
                limit=limit,
                offset=offset,
                message="Data fetched successfully"
            )
        )

    @staticmethod
    def get_one(id):
        music = Music.objects.filter(id=id).first()
        if not music:
            return Response(
                Utils.error_response("Music not found", f"id {id} does not exist"),
                status=404
            )
        data = MusicResponse(music).data
        return Response(Utils.success_response("Data fetched successfully", data))

    @staticmethod
    def update(id, data):
        music = Music.objects.filter(id=id).first()
        if not music:
            return Response(
                Utils.error_response("Music not found", f"id {id} does not exist"),
                status=404
            )

        update_data = asdict(data)

        if update_data.get("singer") is not None:
            singer = Singer.get_by_name(update_data["singer"])
            if not singer:
                return Response(
                    Utils.error_response(
                        "Singer not found",
                        f"singer_name '{update_data['singer']}' does not exist"
                    ),
                    status=status.HTTP_404_NOT_FOUND
                )
            music.singer = singer

        for field in ["song_name", "description"]:
            value = update_data.get(field)
            if value is not None:
                setattr(music, field, value)

        music.save()
        data = MusicResponse(music).data
        return Response(Utils.success_response("Music updated successfully", data))

    @staticmethod
    def delete(id):
        music = Music.objects.filter(id=id).first()
        if not music:
            return Response(
                Utils.error_response("Music not found", f"id {id} does not exist"),
                status=404
            )

        music.delete()
        return Response(Utils.success_response("Music deleted successfully"))
