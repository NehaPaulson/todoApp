from dataclasses import asdict
from rest_framework.response import Response
from rest_framework import status

from feature.music.model.models import Music
from feature.music.serializer.response.music_response import MusicResponse


class MusicView:

    @staticmethod
    def create(data):
        music = Music.objects.create(
            song_name=data.song_name,
            description=data.description,
            singer=data.singer,
        )
        return Response(MusicResponse(music).data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_all():
        musics = Music.objects.all()
        return Response(MusicResponse(musics, many=True).data)

    @staticmethod
    def get_one(id):
        music = Music.objects.filter(id=id).first()
        if not music:
            return Response({"message": "Not found"}, status=404)
        return Response(MusicResponse(music).data)

    @staticmethod
    def update(id, data):
        music = Music.objects.filter(id=id).first()
        if not music:
            return Response({"message": "Not found"}, status=404)

        # ✅ FIX IS HERE
        for field, value in asdict(data).items():
            if value is not None:
                setattr(music, field, value)

        music.save()
        return Response(MusicResponse(music).data)

    @staticmethod
    def delete(id):
        music = Music.objects.filter(id=id).first()
        if not music:
            return Response({"message": "Not found"}, status=404)

        music.delete()
        return Response({"message": "Deleted successfully"})
