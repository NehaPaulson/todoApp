from dataclasses import asdict

from feature.music.model.models import Music
from feature.singer.model.models import Singer
from feature.common.common import Common
from feature.music.serializer.response.music_response import MusicResponse


class MusicView:

    @Common(
        response_handler=MusicResponse,
        message="Music created successfully"
    ).exception_handler
    def create(self, params):
        singer = Singer.get_by_name(params.singer)
        if not singer:
            raise ValueError(f"singer_name '{params.singer}' does not exist")

        return Music.objects.create(
            song_name=params.song_name,
            description=params.description,
            singer=singer
        )

    @Common(
        response_handler=MusicResponse,
        message="Data fetched successfully"
    ).exception_handler
    def get_all(self, request):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        queryset = Music.objects.all()
        return queryset[offset: offset + limit]

    @Common(
        response_handler=MusicResponse,
        message="Data fetched successfully"
    ).exception_handler
    def get_one(self, music_id: int):
        music = Music.objects.filter(id=music_id).first()
        if not music:
            raise ValueError(f"id {music_id} does not exist")
        return music

    @Common(
        response_handler=MusicResponse,
        message="Music updated successfully"
    ).exception_handler
    def update(self, music_id: int, params):
        music = Music.objects.filter(id=music_id).first()
        if not music:
            raise ValueError(f"id {music_id} does not exist")

        data = asdict(params)

        if data.get("singer"):
            singer = Singer.get_by_name(data["singer"])
            if not singer:
                raise ValueError(f"singer_name '{data['singer']}' does not exist")
            music.singer = singer

        if data.get("song_name") is not None:
            music.song_name = data["song_name"]

        if data.get("description") is not None:
            music.description = data["description"]

        music.save()
        return music

    @Common(
        message="Music deleted successfully"
    ).exception_handler
    def delete(self, music_id: int):
        music = Music.objects.filter(id=music_id).first()
        if not music:
            raise ValueError(f"id {music_id} does not exist")

        music.delete()
        return {}
