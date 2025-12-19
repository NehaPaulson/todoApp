class Utils:
    @staticmethod
    def success_response(message: str = None, data: list | dict = None):
        response = {"status": True}
        if message:
            response["message"] = message
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def warning_response(warning: str, message: str = None, data: list | dict = None):
        response = {"status": True, "warning": warning}
        if message:
            response["message"] = message
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def error_response(message: str, error: str | list[str]):
        return {
            "status": False,
            "message": message,
            "error": error
        }

    # ✅ NEW: limit–offset pagination
    @staticmethod
    def paginated_response(
        *,
        data: list,
        total: int,
        limit: int,
        offset: int,
        message: str = None
    ):
        response = {
            "status": True,
            "data": data,
            "pagination": {
                "limit": limit,
                "offset": offset,
                "total": total,
                "next_offset": offset + limit if offset + limit < total else None,
                "previous_offset": offset - limit if offset - limit >= 0 else None,
            }
        }
        if message:
            response["message"] = message
        return response
