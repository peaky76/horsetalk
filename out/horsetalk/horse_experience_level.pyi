from .parsing_enum import ParsingEnum as ParsingEnum

class HorseExperienceLevel(ParsingEnum):
    MAIDEN: int
    NOVICE: int
    BEGINNER: int
    NOVICES = NOVICE
    BEGINNERS = BEGINNER
