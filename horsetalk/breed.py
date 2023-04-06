from .enum_bases import CaseInsensitiveEnum


class Breed(CaseInsensitiveEnum):
    """
    An enumeration representing a breed of horse.
    """

    THOROUGHBRED = 1
    ARABIAN = 2
    QUARTER_HORSE = 3
    AQPS = 4

    # Abbreviations
    TB = THOROUGHBRED
    QH = QUARTER_HORSE
