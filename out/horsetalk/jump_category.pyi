from .parsing_enum import ParsingEnum as ParsingEnum

class JumpCategory(ParsingEnum):
    HURDLE: int
    STEEPLECHASE: int
    CROSS_COUNTRY: int
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
