from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from feature.music.serializer.request.create_music_request import CreateMusicRequest
from feature.music.serializer.request.update_music_request import UpdateMusicRequest
from feature.music.views import MusicView


class MusicController:

    @staticmethod
    @api_view(["POST"])
    def create(request):
        serializer = CreateMusicRequest(data=request.data)
        if serializer.is_valid():
            return MusicView.create(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(["GET"])
    def get_all(request):
        return MusicView.get_all(request)
    @staticmethod
    @api_view(["GET"])
    def get_one(request, id):
        return MusicView.get_one(id)

    @staticmethod
    @api_view(["PUT"])
    def update(request, id):
        serializer = UpdateMusicRequest(data=request.data)
        if serializer.is_valid():
            return MusicView.update(id, serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(["DELETE"])
    def delete(request, id):
        return MusicView.delete(id)