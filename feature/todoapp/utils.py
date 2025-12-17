class Utils:
    @staticmethod
    def success_response(message: str = None, data: list | dict = None):
        """
        Standard success response
        """
        response = {"status": True}
        if message:
            response["message"] = message
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def warning_response(warning: str, message: str = None, data: list | dict = None):
        """
        Standard warning response
        """
        response = {"status": True, "warning": warning}
        if message:
            response["message"] = message
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def error_response(message: str, error: str | list[str]):
        """
        Standard error response
        """
        return {
            "status": False,
            "message": message,
            "error":error
}