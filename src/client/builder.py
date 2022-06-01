from enum import IntEnum


class RequestType(IntEnum):
    GET = 0
    SHORT = 1
    LONG = 2


class RequestBuilder:
    _type: RequestType
    _data: dict

    def set_type(self, _type: RequestType):
        self._type = _type
        return self

    def set_data(self, data):
        self._data = data
        return self

    def build(self):
        pass
