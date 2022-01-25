from enum import Enum


class RhubapilabclusterrebootHostsJsonBodyType(str, Enum):
    SOFT = "soft"
    HARD = "hard"

    def __str__(self) -> str:
        return str(self.value)
