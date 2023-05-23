from typing import Callable
from horsetalk.parsing_enum import ParsingEnum


class Silks:
    class Colour(ParsingEnum):
        """An enumeration of colours that can appear on jockey silks."""

        BEIGE = 1
        BLACK = 2
        BROWN = 3
        DARK_BLUE = 4
        DARK_GREEN = 5
        EMERALD_GREEN = 6
        GREEN = 7
        GREY = 8
        LIGHT_BLUE = 9
        LIGHT_GREEN = 10
        MAROON = 11
        MAUVE = 12
        ORANGE = 13
        PINK = 14
        PURPLE = 15
        RED = 16
        ROYAL_BLUE = 17
        WHITE = 18
        YELLOW = 19

        @staticmethod
        def phrases():
            return [
                colour.replace("_", " ").lower()
                for colour in Silks.Colour.__members__.keys()
            ]

    class Pattern(ParsingEnum):
        """An enumeration of patterns that can appear on jockey silks."""

        ARMLETS = 1  #
        ARMLET = ARMLETS
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

        @staticmethod
        def phrases():
            return [
                pattern.replace("_", " ").lower()
                for pattern in Silks.Pattern.__members__.keys()
            ]

    class Element:
        def __init__(
            self,
            primary: "Silks.Colour",
            secondary: "Silks.Colour" = None,
            pattern: "Silks.Shape" = None,
        ):
            self.primary = primary
            self.secondary = secondary
            self.pattern = pattern

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
        element = self._convert_to_element(
            self._parts_for_element(lambda parts: parts[0])
        )
        element.secondary = element.secondary or element.primary
        element.pattern = element.pattern or Silks.Pattern.PLAIN
        return element

    @property
    def cap(self) -> "Silks.Element":
        """Returns the cap of the silks.

        Returns:
            A Silks.Element object.
        """
        element = self._convert_to_element(
            self._parts_for_element(lambda parts: next(p for p in parts if "cap" in p))
            if "cap" in self.description
            else []
        )
        return self._apply_defaults(element)

    @property
    def sleeves(self) -> "Silks.Element":
        """Returns the sleeves of the silks.

        Returns:
            A Silks.Element object.
        """
        element = self._convert_to_element(
            self._parts_for_element(
                lambda parts: next(p for p in parts if "sleeves" in p)
            )
            if "sleeves" in self.description
            else []
        )
        return self._apply_defaults(element)

    @property
    def _clauses(self) -> list[str]:
        clauses = [
            Silks._conjoin_words(clause.split(" "))
            for clause in self.description.lower()
            .replace("(", "")
            .replace(")", "")
            .split(", ")
        ]

        to_add = {}
        for i, clause in enumerate(clauses):
            new_clause = None
            while "and" in clause:
                index = clause.index("and")
                before_is_colour = clause[index - 1] in Silks.Colour.phrases()
                after_is_colour = clause[index + 1] in Silks.Colour.phrases()
                # colour and colour
                if before_is_colour and after_is_colour:
                    del clause[index]
                # pattern and element
                # element and element
                else:
                    new_clause = clause[: index - 1] + clause[index + 1 :]
                    clause = clause[:index]

            clauses[i] = clause
            if new_clause:
                to_add[i + 1] = new_clause

        for key in to_add:
            clauses.insert(key, to_add[key])

        return clauses

    def _parts_for_element(self, element_selector: Callable) -> str:
        main_clause = element_selector(self._clauses)
        index = self._clauses.index(main_clause)
        next_clause = (
            self._clauses[index + 1]
            if index + 1 != len(self._clauses)
            and not (
                "cap" in self._clauses[index + 1]
                or "sleeves" in self._clauses[index + 1]
            )
            else []
        )

        return main_clause + next_clause

    def _apply_defaults(self, element: "Silks.Element") -> "Silks.Element":
        element.secondary = (
            element.secondary
            or element.primary
            or (
                self.body.secondary
                if "and" in self._clauses[0]
                or element.pattern
                or self.body.pattern
                not in [Silks.Pattern.PLAIN, Silks.Pattern.EPAULETS]
                else self.body.primary
            )
        )
        element.pattern = element.pattern or (
            Silks.Pattern.PLAIN
            if element.primary or self.body.pattern == Silks.Pattern.EPAULETS
            else self.body.pattern
        )
        element.primary = element.primary or self.body.primary
        return element

    def _convert_to_element(self, words: list[str]) -> "Silks.Element":
        details = [
            (
                Silks.Colour[word]
                if word in Silks.Colour.phrases()
                else Silks.Pattern[word]
                if word in Silks.Pattern.phrases()
                else None
            )
            for word in words
            if word != "cap" and word != "sleeves"
        ]

        details.extend([None] * (3 - len(details)))
        details.sort(
            key=lambda x: (
                isinstance(x, Silks.Pattern),
                x is None,
                isinstance(x, Silks.Colour),
            )
        )

        return Silks.Element(*details)

    def _conjoin_words(words: list[str]) -> list[str]:
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

        while any(word in words for word in FIRST_WORDS):
            index = words.index(next(word for word in words if word in FIRST_WORDS))
            words = (
                words[:index]
                + [" ".join([words[index], words[index + 1]])]
                + words[index + 2 :]
            )

        return words
