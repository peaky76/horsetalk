from peak_utility.enumeration.parsing_enum import ParsingEnum  # type: ignore as ParsingEnum

class HorseExperienceLevel(ParsingEnum):
    MAIDEN: int
    NOVICE: int
    BEGINNER: int
    NOVICES = NOVICE
    BEGINNERS = BEGINNER
