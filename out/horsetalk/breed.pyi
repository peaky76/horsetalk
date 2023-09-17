from peak_utility.enumeration.parsing_enum import ParsingEnum  # type: ignore as ParsingEnum

class Breed(ParsingEnum):
    THOROUGHBRED: int
    ARABIAN: int
    QUARTER_HORSE: int
    AQPS: int
    TB = THOROUGHBRED
    QH = QUARTER_HORSE
