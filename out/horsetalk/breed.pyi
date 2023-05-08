from .parsing_enum import ParsingEnum as ParsingEnum

class Breed(ParsingEnum):
    THOROUGHBRED: int
    ARABIAN: int
    QUARTER_HORSE: int
    AQPS: int
    TB = THOROUGHBRED
    QH = QUARTER_HORSE
