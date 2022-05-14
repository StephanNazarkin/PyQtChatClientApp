from Exceptions.AppException import Error


class ResponseIsFalseException(Error):
    """Raised when the response is false"""

    def __init__(self, message="Error: Response is false"):
        self.message = message
        super().__init__(self.message)

