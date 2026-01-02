from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.singer.views import SingerView
from feature.singer.serializer.request.create_singer_request import CreateSingerRequestSerializer
from feature.singer.serializer.request.update_singer_request import UpdateSingerRequestSerializer
from feature.singer.serializer.request.get_all_singer_request import GetAllSingerRequestSerializer
from feature.singer.serializer.request.get_one_singer_request import GetOneSingerRequestSerializer
from feature.singer.serializer.request.delete_singer_request import DeleteSingerRequestSerializer


view = SingerView()


@api_view(["POST"])
def create(request: Request):
    serializer = CreateSingerRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    params = serializer.save()
    return view.create(params)


@api_view(["GET"])
def get_all(request: Request):
    serializer = GetAllSingerRequestSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    return view.get_all(request)


@api_view(["GET"])
def get_one(request: Request, id: int):
    serializer = GetOneSingerRequestSerializer(data={"id": id})
    serializer.is_valid(raise_exception=True)
    return view.get_one(id)


@api_view(["PUT"])
def update(request: Request, id: int):
    serializer = UpdateSingerRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    params = serializer.save()
    return view.update(id, params)


@api_view(["DELETE"])
def delete(request: Request, id: int):
    serializer = DeleteSingerRequestSerializer(data={"id": id})
    serializer.is_valid(raise_exception=True)
    return view.delete(id)
