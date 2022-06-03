from enum import Enum


class RequestTypeCode(Enum):
    GET = 0x00
    SHORT = 0x01
    LONG = 0x02
    JSON = 0x03
