from src.сonstants import *
from dataclasses import dataclass


@dataclass
class RequestBuilder:
    _type: RequestTypeCode
    _data: dict

    def build(self):
        pass
