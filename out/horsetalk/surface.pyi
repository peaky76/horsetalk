from peak_utility.enumeration.parsing_enum import ParsingEnum as ParsingEnum

class Surface(ParsingEnum):
    TURF: int
    DIRT: int
    ALL_WEATHER: int
    T = TURF
    D = DIRT
    AW = ALL_WEATHER
