from Exceptions.AppException import Error


class IncorrectPasswordException(BaseException):
    """Raised when the response is false"""

    def __init__(self, message="Error: Bad Request"):
        self.message = message
        super().__init__(self.message)