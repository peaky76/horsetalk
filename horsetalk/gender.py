from .parsing_enum import ParsingEnum
from .sex import Sex


class Gender(ParsingEnum):
    """
    An enumeration representing the gender of a horse.

    """

    FOAL = 0
    YEARLING = 1
    COLT = 2
    FILLY = 3
    STALLION = 4
    MARE = 5
    GELDING = 6
    RIG = 7

    # Abbreviations
    C = COLT
    F = FILLY
    S = STALLION
    M = MARE
    G = GELDING
    R = RIG

    # Plural
    FOALS = FOAL
    YEARLINGS = YEARLING
    COLTS = COLT
    FILLIES = FILLY
    STALLIONS = STALLION
    MARES = MARE
    GELDINGS = GELDING
    RIGS = RIG

    @property
    def sex(self):
        if self in [Gender.FOAL, Gender.YEARLING]:
            raise ValueError("Not enough information to provide sex of horse")

        return Sex.FEMALE if self in [Gender.FILLY, Gender.MARE] else Sex.MALE

    @staticmethod
    def determine(sex: Sex, official_age: int, **kwargs):
        if official_age == 0:
            return Gender.FOAL
        if official_age == 1:
            return Gender.YEARLING
        if kwargs.get("is_gelded"):
            if sex is sex.FEMALE:
                raise ValueError("Female horse cannot be gelded")
            return Gender.GELDING
        if kwargs.get("is_rig"):
            if sex is sex.FEMALE:
                raise ValueError("Female horse cannot be rig")
            return Gender.RIG
        if official_age <= 3:
            return Gender.COLT if sex is sex.MALE else Gender.FILLY
        else:
            return Gender.STALLION if sex is sex.MALE else Gender.MARE
