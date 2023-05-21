from enum import auto
from horsetalk.parsing_enum import ParsingEnum


class Silks:
    class Colour(ParsingEnum):
        """An enumeration of colours that can appear on jockey silks."""

        BEIGE = auto()
        BLACK = auto()
        BROWN = auto()
        DARK_BLUE = auto()
        EMERALD_GREEN = auto()
        GREEN = auto()
        GREY = auto()
        LIGHT_BLUE = auto()
        LIGHT_GREEN = auto()
        MAROON = auto()
        MAUVE = auto()
        ORANGE = auto()
        PINK = auto()
        PURPLE = auto()
        RED = auto()
        ROYAL_BLUE = auto()
        WHITE = auto()
        YELLOW = auto()

    class Pattern(ParsingEnum):
        """An enumeration of patterns that can appear on jockey silks."""

        ARMLET = auto()
        BRACES = auto()  #
        CHECK = auto()  #
        CHEVRON = auto()  #
        CHEVRONS = auto()  #
        CROSS_BELTS = auto()  #
        CROSS_OF_LORRAINE = auto()  #
        CROSS_SASHES = CROSS_BELTS
        CUFFS = auto()
        DIAMOND = auto()  #
        DIAMONDS = auto()  #
        DIABOLO = auto()  #
        DISC = auto()  #
        EPAULETS = auto()  #
        HALVED = auto()
        HOLLOW_BOX = auto()  #
        HOOP = auto()  #
        HOOPS = auto()  #
        INVERTED_TRIANGLE = auto()  #
        LARGE_SPOTS = auto()  #
        PANEL = auto()
        PLAIN = auto()  #
        QUARTERED = auto()  #
        SASH = auto()
        SEAMS = auto()  #
        SPOTS = auto()  #
        STAR = auto()  #
        STARS = auto()  #
        STRIPE = auto()  #
        STRIPES = auto()  #
        STRIPED = STRIPES
        TRIPLE_DIAMOND = auto()  #

    class Element:
        def __init__(
            self,
            primary: "Silks.Colour",
            pattern: "Silks.Shape" = None,
            secondary: "Silks.Colour" = None,
        ):
            self.primary = primary
            self.pattern = pattern if pattern else Silks.Pattern.PLAIN
            self.secondary = secondary if secondary else self.primary

        def __eq__(self, other):
            return (
                self.primary == other.primary
                and self.pattern == other.pattern
                and self.secondary == other.secondary
            )

    @classmethod
    def parse(cls, description: str) -> dict:
        """Parses a description of silks into component parts.

        Args:
            description: A description of silks.
        """
        self = cls()
        self.description = description

        return {"body": None, "sleeves": self.sleeves, "cap": self.cap}

    @property
    def cap(self):
        for part in self._parts():
            if "cap" in part:
                detail = (
                    part.replace("cap", "")
                    .replace("sleeves", "")
                    .replace("and", "")
                    .strip()
                )
                return Silks.Element(Silks.Colour[detail])

        return None

    @property
    def sleeves(self):
        for part in self._parts():
            if "sleeves" in part:
                detail = (
                    part.replace("cap", "")
                    .replace("sleeves", "")
                    .replace("and", "")
                    .strip()
                )
                return Silks.Element(Silks.Colour[detail])

        return None

    def _parts(self):
        return self.description.lower().split(", ")
