from .enum_bases import SpaceAndCaseInsensitiveEnum


class Obstacle(SpaceAndCaseInsensitiveEnum):
    """
    An enumeration representing the type of obstacle a race takes place over
    """

    HURDLE = 1
    STEEPLECHASE = 2
    CROSS_COUNTRY = 3

    # Abbreviations
    H = HURDLE
    HRD = HURDLE
    HRDLE = HURDLE
    C = STEEPLECHASE
    CH = STEEPLECHASE
    CHS = STEEPLECHASE
    CHSE = STEEPLECHASE
    CHASE = STEEPLECHASE
    CC = CROSS_COUNTRY
    XC = CROSS_COUNTRY
