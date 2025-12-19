from rest_framework.response import Response
from feature.todoapp.serializer.response.todo_response import TodoResponseSerializer
from feature.todoapp.model.models import Todo
from feature.common.utils import Utils


class TodoView:

    def create(self, params):
        todo = Todo.create(
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Todo created successfully", data))

    def get_all(self, request):
        limit = int(request.query_params.get("limit", 10))
        offset = int(request.query_params.get("offset", 0))

        queryset = Todo.get_all()
        total = queryset.count()

        todos = queryset[offset: offset + limit]
        data = TodoResponseSerializer(todos, many=True).data

        return Response(
            Utils.paginated_response(
                data=data,
                total=total,
                limit=limit,
                offset=offset,
                message="Data fetched successfully"
            )
        )

    def get_one(self, todo_id: int):
        todo = Todo.get_one(todo_id)
        if not todo:
            return Response(
                Utils.error_response("Todo not found", f"id {todo_id} does not exist"),
                status=404
            )
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Data fetched successfully", data))

    def update(self, todo_id, params):
        todo = Todo.update(
            todo_id,
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        if not todo:
            return Response(
                Utils.error_response("Todo not found", f"id {todo_id} does not exist"),
                status=404
            )
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Todo updated successfully", data))

    def delete(self, todo_id: int):
        success = Todo.delete_one(todo_id)
        if not success:
            return Response(
                Utils.error_response("Todo not found", f"id {todo_id} does not exist"),
                status=404
            )
        return Response(Utils.success_response("Todo deleted successfully"))
