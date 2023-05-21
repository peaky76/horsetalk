from enum import auto
from horsetalk.parsing_enum import ParsingEnum


class Silks:
    class Shape(ParsingEnum):
        """An enumeration of shapes that can appear on jockey silks."""

        ARMLET = auto()
        BRACES = auto()
        CHECK = auto()
        CHEVRON = auto()
        CHEVRONS = auto()
        CROSS_OF_LORRAINE = auto()
        CROSS_SASHES = auto()
        CUFFS = auto()
        DIAMOND = auto()
        DIABOLO = auto()
        DISC = auto()
        EPAULETS = auto()
        HALVED = auto()
        HOOP = auto()
        HOOPS = auto()
        INVERTED_TRIANGLE = auto()
        PANEL = auto()
        QUARTERED = auto()
        SASH = auto()
        SEAMS = auto()
        SPOTS = auto()
        STAR = auto()
        STARS = auto()
        STRIPE = auto()
        STRIPED = auto()
        TRIPLE_DIAMOND = auto()

    @classmethod
    def parse(cls, description: str) -> dict:
        """Parses a description of silks into component parts.

        Args:
            description: A description of silks.
        """
        self = cls()
        self.description = description

        return {"shirt": None, "sleeves": None, "cap": None}
