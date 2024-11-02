from enum import Enum


class UserPrivilegePrivilege(str, Enum):
    CUSTOM = "CUSTOM"
    NONE = "NONE"
    OWNER = "OWNER"
    TRADER = "TRADER"

    def __str__(self) -> str:
        return str(self.value)
