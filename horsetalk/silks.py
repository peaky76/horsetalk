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
            return [colour.name.replace("_", " ").lower() for colour in Silks.Colour]

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
            return [pattern.name.replace("_", " ").lower() for pattern in Silks.Pattern]

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
        return self._convert_to_element(self._parts_for_element(""))

    @property
    def cap(self) -> "Silks.Element":
        """Returns the cap of the silks.

        Returns:
            A Silks.Element object.
        """
        element = self._convert_to_element(self._parts_for_element("cap"))
        return self._apply_defaults(element)

    @property
    def sleeves(self) -> "Silks.Element":
        """Returns the sleeves of the silks.

        Returns:
            A Silks.Element object.
        """
        element = self._convert_to_element(self._parts_for_element("sleeves"))
        return self._apply_defaults(element)

    @property
    def _parts(self) -> list[str]:
        return self.description.lower().split(", ")

    def _parts_for_element(self, element: str = "") -> str:
        parts = self.description.lower().split(", ")
        named_part = lambda part: "cap" in part or "sleeves" in part

        main_part = None
        next_part = None
        for i, part in enumerate(parts):
            if element in part:
                main_part = part
                next_part = (
                    parts[i + 1]
                    if i + 1 != len(parts)
                    and (
                        not named_part(parts[i + 1])
                        or (element == "" and " and sleeves" in parts[i + 1])
                    )
                    else None
                )
                break

        WORDS_TO_REMOVE = ["cap", "sleeves", " and", " on", "(", ")"]

        parts = " ".join([main_part, next_part]) if next_part else main_part
        for word in WORDS_TO_REMOVE:
            parts = parts.replace(word, "")

        return parts.strip()

    def _apply_defaults(self, element: "Silks.Element") -> "Silks.Element":
        element.primary = element.primary or self.body.primary
        element.secondary = element.secondary or self.body.secondary
        element.pattern = element.pattern or self.body.pattern
        return element

    def _convert_to_element(self, part: str) -> "Silks.Element":
        details = []
        words = Silks._conjoin_words(part.split(" "))
        for word in words:
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
