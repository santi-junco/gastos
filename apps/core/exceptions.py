from rest_framework.exceptions import APIException

class CustomException(APIException):
    def __init__(self, detail="ERROR", code=400):
        self.default_detail = detail
        self.status_code = code
        super().__init__(detail, code)
