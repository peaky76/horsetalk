from peak_utility.enumeration.parsing_enum import ParsingEnum  # type: ignore as ParsingEnum

class ObstacleStyle(ParsingEnum):
    HURDLE: int
    PLAIN_FENCE: int
    OPEN_DITCH: int
    WATER_JUMP: int
    SPECIALIST: int
    PLAIN = PLAIN_FENCE
    DITCH = OPEN_DITCH
    WATER = WATER_JUMP
