from .enum_bases import SpaceAndCaseInsensitiveEnum


class Surface(SpaceAndCaseInsensitiveEnum):
    """
    An enumeration representing the surface upon which races are held
    """

    TURF = 1
    DIRT = 2
    ALL_WEATHER = 3

    # Abbreviations
    T = TURF
    D = DIRT
    AW = ALL_WEATHER
