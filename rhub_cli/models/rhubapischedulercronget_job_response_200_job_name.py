from enum import Enum


class RhubapischedulercrongetJobResponse200JobName(str, Enum):
    EXAMPLE = "example"
    TOWER_LAUNCH = "tower_launch"

    def __str__(self) -> str:
        return str(self.value)
