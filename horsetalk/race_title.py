from enum import Enum
from typing import List, Type
from .age_category import AgeCategory
from .experience_level import ExperienceLevel
from .obstacle import Obstacle
from .weight_determinant import WeightDeterminant


class RaceTitle:
    _words: List[str] = []

    @classmethod
    def parse(cls, title: str) -> dict:
        """Parse a race title into component parts

        :param title: A race title
        :type title: str
        :return: A dictionary of component parts
        :rtype: dict
        """
        self = cls()
        self._words = title.split()
        return {
            "age_category": x[-1] if (x := self._lookup(AgeCategory)) else None,
            "experience_level": x[-1] if (x := self._lookup(ExperienceLevel)) else None,
            "obstacle": x[-1] if (x := self._lookup(Obstacle)) else None,
            "weight_determinant": x[-1]
            if (x := self._lookup(WeightDeterminant))
            else None,
        }

    def _lookup(self, enum: Type[Enum]) -> List[Enum]:
        """Private method to lookup an enum value from a list of words

        :param enum: Enum to search through
        :type enum: Type[Enum]
        :return: The found Enum value or None
        :rtype: Enum | None
        """
        return [
            found_value
            for word in self._words
            if (found_value := getattr(enum, word, None)) is not None
        ]
