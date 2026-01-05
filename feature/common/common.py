from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from feature.common.utils import Utils
from django.db.models.query import QuerySet


class Common:
    def __init__(self, *, response_handler=None, message=None):
        self.response_handler = response_handler
        self.message = message

    def exception_handler(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                # If view already returned Response → pass through
                if isinstance(result, Response):
                    return result

                many = isinstance(result, (list, tuple, QuerySet))

                # Apply response serializer if provided
                if self.response_handler:
                    serializer = self.response_handler(result, many=many)
                    result = serializer.data

                return Response(
                    Utils.success_response(
                        message=self.message,
                        data=result
                    ),
                    status=status.HTTP_200_OK
                )

            except ValueError as e:
                return Response(
                    Utils.error_response("Validation error", str(e)),
                    status=status.HTTP_400_BAD_REQUEST
                )

            except Exception as e:
                return Response(
                    Utils.error_response("Something went wrong", str(e)),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return wrapper
