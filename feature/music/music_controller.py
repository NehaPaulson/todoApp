from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.music.views import MusicView
from feature.music.serializer.request.create_music_request import CreateMusicRequest
from feature.music.serializer.request.update_music_request import UpdateMusicRequest
from feature.music.serializer.request.get_all_music_request import GetAllMusicRequestSerializer
from feature.music.serializer.request.get_one_music_request import GetOneMusicRequestSerializer
from feature.music.serializer.request.delete_music_request import DeleteMusicRequestSerializer


view = MusicView()


class MusicController:

    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateMusicRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.save()
        return view.create(params)

    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        serializer = GetAllMusicRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        return view.get_all(request)

    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request, id: int):
        serializer = GetOneMusicRequestSerializer(data={"id": id})
        serializer.is_valid(raise_exception=True)

        return view.get_one(id)

    @staticmethod
    @api_view(["PUT"])
    def update(request: Request, id: int):
        serializer = UpdateMusicRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = serializer.save()
        return view.update(id, params)

    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request, id: int):
        serializer = DeleteMusicRequestSerializer(data={"id": id})
        serializer.is_valid(raise_exception=True)

        return view.delete(id)
