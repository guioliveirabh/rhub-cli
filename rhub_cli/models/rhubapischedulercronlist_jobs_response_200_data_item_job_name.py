from enum import Enum


class RhubapischedulercronlistJobsResponse200DataItemJobName(str, Enum):
    EXAMPLE = "example"
    TOWER_LAUNCH = "tower_launch"

    def __str__(self) -> str:
        return str(self.value)
