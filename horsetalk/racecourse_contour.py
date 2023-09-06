from .parsing_enum import ParsingEnum


class RacecourseContour(ParsingEnum):
    """
    An enumeration representing the contour of a racecourse.

    """

    UNKNOWN = 0
    FLAT = 1
    DOWNHILL = 2
    UPHILL = 3
    UNDULATING = 4

    # Alternatives
    DOWN = DOWNHILL
    UP = UPHILL
