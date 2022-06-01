import socket

from src.exceptions import OversizeError

PORT = 2000
SHORT_DATA_SIZE = 16
LONG_DATA_SIZE = 32


def get(hostname: str, uri: str, data: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((hostname, PORT))
        request = list()
        request.append(0x00)
        # TODO


def short(hostname: str, urid: int, data: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((hostname, PORT))
        request = list()
        request.append(0x01)
        request.extend(urid.to_bytes(8, "big"))
        request.extend(bytes(data, "utf-8"))
        s.send(bytes(request))


def long(hostname: str, urid: int, data: str):
    data_b = list(bytes(data, "utf-8"))
    if len(data_b) > LONG_DATA_SIZE:
        raise OversizeError("long")
    elif len(data_b) < LONG_DATA_SIZE:
        for i in range(LONG_DATA_SIZE - len(data_b)):
            data_b.append(0)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((hostname, PORT))
        request = list()
        request.append(0x02)
        request.extend(urid.to_bytes(8, "big"))
        request.extend(data_b)
        s.send(bytes(request))
