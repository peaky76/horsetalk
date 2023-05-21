from enum import auto
from horsetalk.parsing_enum import ParsingEnum


class Silks:
    class Colour(ParsingEnum):
        """An enumeration of colours that can appear on jockey silks."""

        BEIGE = 1
        BLACK = 2
        BROWN = 3
        DARK_BLUE = 4
        EMERALD_GREEN = 5
        GREEN = 6
        GREY = 7
        LIGHT_BLUE = 8
        LIGHT_GREEN = 9
        MAROON = 10
        MAUVE = 11
        ORANGE = 12
        PINK = 13
        PURPLE = 14
        RED = 15
        ROYAL_BLUE = 16
        WHITE = 17
        YELLOW = 18

    class Pattern(ParsingEnum):
        """An enumeration of patterns that can appear on jockey silks."""

        ARMLET = 1
        BRACES = 2  #
        CHECK = 3  #
        CHEVRON = 4  #
        CHEVRONS = 5  #
        CROSS_BELTS = 6  #
        CROSS_OF_LORRAINE = 7  #
        CROSS_SASHES = CROSS_BELTS
        CUFFS = 8
        DIAMOND = 9  #
        DIAMONDS = 10  #
        DIABOLO = 11  #
        DISC = 12  #
        EPAULETS = 13  #
        HALVED = 14
        HOLLOW_BOX = 15  #
        HOOP = 16  #
        HOOPS = 17  #
        HOOPED = HOOPS
        INVERTED_TRIANGLE = 18  #
        LARGE_SPOTS = 19  #
        PANEL = 20
        PLAIN = 21  #
        QUARTERED = 22  #
        SASH = 23
        SEAMS = 24  #
        SPOTS = 25  #
        STAR = 26  #
        STARS = 27  #
        STRIPE = 28  #
        STRIPES = 29  #
        STRIPED = STRIPES
        TRIPLE_DIAMOND = 30  #

    class Element:
        def __init__(
            self,
            primary: "Silks.Colour",
            secondary: "Silks.Colour" = None,
            pattern: "Silks.Shape" = None,
        ):
            self.primary = primary
            self.secondary = secondary if secondary else self.primary
            self.pattern = pattern if pattern else Silks.Pattern.PLAIN

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

        return {"body": self.body, "sleeves": self.sleeves, "cap": self.cap}

    @property
    def body(self):
        body_parts = " ".join(
            [
                part
                for part in self._parts()
                if "cap" not in part and "sleeves" not in part
            ]
        )

        return self._convert_to_element(body_parts)

    @property
    def cap(self):
        for part in self._parts():
            if "cap" in part:
                return self._convert_to_element(part)

        return None

    @property
    def sleeves(self):
        for part in self._parts():
            if "sleeves" in part:
                return self._convert_to_element(part)

        return None

    def _parts(self):
        return self.description.lower().split(", ")

    def _convert_to_element(self, part: str):
        details = []
        for word in self._words(part):
            try:
                detail = Silks.Colour[word]
            except KeyError:
                try:
                    detail = Silks.Pattern[word]
                except KeyError:
                    detail = None

            if detail is not None:
                details.append(detail)

        return Silks.Element(*details)

    def _words(self, part: str):
        FIRST_WORDS = [
            "dark",
            "light",
            "royal",
            "emerald",
            "cross",
            "cross of",
            "inverted",
            "large",
            "triple",
        ]

        words = (
            part.lower()
            .replace("cap", "")
            .replace("sleeves", "")
            .replace(" and ", " ")
            .replace(" on ", " ")
            .strip()
            .split(" ")
        )

        while any(word in words for word in FIRST_WORDS):
            index = words.index(next(word for word in words if word in FIRST_WORDS))
            words = (
                words[:index]
                + [" ".join([words[index], words[index + 1]])]
                + words[index + 2 :]
            )

        return words
