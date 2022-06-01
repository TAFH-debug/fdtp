from typing import Literal


class OversizeError(BaseException):
    def __init__(self, req_type: Literal['short', 'long']):
        if req_type != 'short' or req_type != 'long':
            self.type = "undefined"
            return
        self.type = req_type
