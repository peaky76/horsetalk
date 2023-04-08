from .parsing_enum import ParsingEnum


class AWGoingDescription(ParsingEnum):
    """
    An enumeration that represents a scale of UK and Ireland all-weather going descriptions.

    """

    SLOW = 1
    STANDARD_TO_SLOW = 2
    STANDARD = 3
    STANDARD_TO_FAST = 4
    FAST = 5

    # Abbreviations
    SLW = SLOW
    STS = STANDARD_TO_SLOW
    STD = STANDARD
    STF = STANDARD_TO_FAST
    FST = FAST