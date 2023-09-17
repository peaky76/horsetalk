from peak_utility.enumeration.parsing_enum import ParsingEnum  # type: ignore as ParsingEnum

class AgeCategory(ParsingEnum):
    JUVENILE: int
    VETERAN: int
    VETERANS = VETERAN
