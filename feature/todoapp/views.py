from feature.todoapp.model.models import Todo
from feature.common.common import Common
from feature.todoapp.serializer.response.todo_response import TodoResponseSerializer


class TodoView:

    @Common(
        response_handler=TodoResponseSerializer,
        message="Todo created successfully"
    ).exception_handler
    def create(self, params):
        return Todo.create(
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )


    @Common(
        response_handler=TodoResponseSerializer,
        message="Data fetched successfully"
    ).exception_handler
    def get_all(self, request):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        queryset = Todo.get_all()
        return queryset[offset: offset + limit]


    @Common(
        response_handler=TodoResponseSerializer,
        message="Data fetched successfully"
    ).exception_handler
    def get_one(self, todo_id: int):
        todo = Todo.get_one(todo_id)
        if not todo:
            raise ValueError(f"id {todo_id} does not exist")
        return todo


    @Common(
        response_handler=TodoResponseSerializer,
        message="Todo updated successfully"
    ).exception_handler
    def update(self, todo_id, params):
        todo = Todo.update(
            todo_id,
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        if not todo:
            raise ValueError(f"id {todo_id} does not exist")
        return todo


    @Common(message="Todo deleted successfully").exception_handler
    def delete(self, todo_id: int):
        success = Todo.delete_one(todo_id)
        if not success:
            raise ValueError(f"id {todo_id} does not exist")
        return {"deleted": True}
