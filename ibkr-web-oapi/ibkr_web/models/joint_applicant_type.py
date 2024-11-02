from enum import Enum


class JointApplicantType(str, Enum):
    AU_JOINT_ACCOUNT = "au_joint_account"
    COMMUNITY = "community"
    JOINT_TENANTS = "joint_tenants"
    TBE = "tbe"
    TENANTS_COMMON = "tenants_common"

    def __str__(self) -> str:
        return str(self.value)
