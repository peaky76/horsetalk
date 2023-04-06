from enum import Enum
from .case_insensitive_enum import CaseInsensitiveEnumMeta


class SurfaceEnumMeta(CaseInsensitiveEnumMeta):
    def __getitem__(cls, name):
        return super().__getitem__(name.replace("-", " ").replace(" ", "_"))


class Surface(Enum, metaclass=SurfaceEnumMeta):
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
