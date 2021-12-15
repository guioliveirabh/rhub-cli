from enum import Enum


class RhubapihealthpingResponse200(str, Enum):
    PONG = "pong"

    def __str__(self) -> str:
        return str(self.value)
