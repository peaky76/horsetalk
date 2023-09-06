from .parsing_enum import ParsingEnum


class RacecourseShape(ParsingEnum):
    UNKNOWN = 0
    STRAIGHT = 1
    HORSESHOE = 2
    TRIANGLE = 3
    OVAL = 4
    PEAR = 5

    # Alternatives
    ROUND = OVAL
    TRIANGULAR = TRIANGLE
