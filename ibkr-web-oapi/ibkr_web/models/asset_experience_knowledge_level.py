from enum import Enum


class AssetExperienceKnowledgeLevel(str, Enum):
    EXTENSIVE = "Extensive"
    GOOD = "Good"
    LIMITED = "Limited"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
