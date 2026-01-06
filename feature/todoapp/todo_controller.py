from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.todoapp.views import TodoView
from feature.todoapp.serializer.request.create_todo_request import CreateTodoRequestSerializer
from feature.todoapp.serializer.request.update_todo_request import UpdateTodoRequestSerializer
from feature.todoapp.serializer.request.get_all_todo_request import GetAllTodoRequestSerializer
from feature.todoapp.serializer.request.get_one_todo_request import GetOneTodoRequestSerializer
from feature.todoapp.serializer.request.delete_todo_request import DeleteTodoRequestSerializer
from drf_spectacular.utils import extend_schema
from feature.todoapp.serializer.response.todo_response import TodoResponseSerializer



view = TodoView()

@extend_schema(
    summary="Create Todo",
    description="Create a new todo item",
    request=CreateTodoRequestSerializer,
    responses=TodoResponseSerializer
)
@api_view(["POST"])
def create(request: Request):
    serializer = CreateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()
    return view.create(params)

@extend_schema(
    summary="Get all todos",
    description="Get all todos with limit and offset",
)
@api_view(["GET"])
def get_all(request: Request):
    serializer = GetAllTodoRequestSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    return view.get_all(request)

@extend_schema(
    summary="Get todo by id",
    description="Get a single todo using id",
)
@api_view(["GET"])
def get_one(request: Request, id: int):
    serializer = GetOneTodoRequestSerializer(data={"id": id})
    serializer.is_valid(raise_exception=True)

    return view.get_one(id)

@extend_schema(
    summary="Update todo",
    description="Update a todo using id",
    request=UpdateTodoRequestSerializer,
    responses=TodoResponseSerializer
)
@api_view(["PUT"])
def update(request: Request, id: int):
    serializer = UpdateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()
    return view.update(id, params)

@extend_schema(
    summary="Delete todo",
    description="Delete todo by id",
)
@api_view(["DELETE"])
def delete(request: Request, id: int):
    serializer = DeleteTodoRequestSerializer(data={"id": id})
    serializer.is_valid(raise_exception=True)

    return view.delete(id)
