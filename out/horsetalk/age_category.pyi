from .parsing_enum import ParsingEnum as ParsingEnum

class AgeCategory(ParsingEnum):
    JUVENILE: int
    VETERAN: int
    VETERANS = VETERAN
