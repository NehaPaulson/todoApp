from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.todoapp.views import TodoView
from feature.todoapp.serializer.request.create_todo_request import CreateTodoRequestSerializer
from feature.todoapp.serializer.request.update_todo_request import UpdateTodoRequestSerializer


view = TodoView()


@api_view(["POST"])
def create(request: Request):
    serializer = CreateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()
    return view.create(params)


@api_view(["GET"])
def get_all(request: Request):
    return view.get_all(request)


@api_view(["GET"])
def get_one(request: Request, id: int):
    return view.get_one(id)


@api_view(["PUT"])
def update(request: Request, id: int):
    serializer = UpdateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()
    return view.update(id, params)


@api_view(["DELETE"])
def delete(request: Request, id: int):
    return view.delete(id)
