from enum import auto
from typing import Any, Callable
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

        def __repr__(self):
            return f"Element(primary={self.primary}, secondary={self.secondary}, pattern={self.pattern})"

        def __eq__(self, other):
            return (
                self.primary == other.primary
                and self.pattern == other.pattern
                and self.secondary == other.secondary
            )

    @classmethod
    def parse(cls, description: str) -> "Silks":
        """Parses a description of silks into component parts.

        Args:
            description: A description of silks.

        Returns:
            A Silks object.
        """
        self = cls()
        self.description = description

        return self

    @property
    def body(self) -> "Silks.Element":
        """Returns the body of the silks.

        Returns:
            A Silks.Element object.
        """
        main_part = self._main_part(lambda part: self._parts().index(part) == 0)
        parts = (
            main_part
            if (next_part := self._next_part(main_part)) is None
            or "cap" in next_part
            or "sleeves" in next_part
            else " ".join([main_part, next_part])
        )
        return self._convert_to_element(parts)

    @property
    def cap(self) -> "Silks.Element":
        """Returns the cap of the silks.

        Returns:
            A Silks.Element object.
        """
        main_part = self._main_part(lambda part: "cap" in part)
        parts = (
            main_part
            if (next_part := self._next_part(main_part)) is None
            else " ".join([main_part, next_part])
        )

        element = self._convert_to_element(parts)
        return self._apply_defaults(element)

    @property
    def sleeves(self) -> "Silks.Element":
        """Returns the sleeves of the silks.

        Returns:
            A Silks.Element object.
        """
        main_part = self._main_part(lambda part: "sleeves" in part)
        parts = (
            main_part
            if (next_part := self._next_part(main_part)) is None or "cap" in next_part
            else " ".join([main_part, next_part])
        )

        element = self._convert_to_element(parts)
        return self._apply_defaults(element)

    def _parts(self):
        return self.description.lower().split(", ")

    def _main_part(self, condition: Callable):
        return next(part for part in self._parts() if condition(part))

    def _next_part(self, main_part: str):
        next_index = self._parts().index(main_part) + 1
        return self._parts()[next_index] if next_index < len(self._parts()) else None

    def _apply_defaults(self, element: "Silks.Element"):
        element.primary = element.primary or self.body.primary
        element.secondary = element.secondary or self.body.secondary
        element.pattern = element.pattern or self.body.pattern
        return element

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

        details = details + [None] * (3 - len(details))
        details.sort(
            key=lambda x: (
                isinstance(x, Silks.Pattern),
                x is None,
                isinstance(x, Silks.Colour),
            )
        )

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
