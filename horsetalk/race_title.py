from enum import Enum
from typing import List, Type
from .experience_level import ExperienceLevel
from .obstacle import Obstacle
from .race_age_status import RaceAgeStatus
from .race_weight_status import RaceWeightStatus


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
            "age_status": self._lookup(RaceAgeStatus),
            "experience_level": self._lookup(ExperienceLevel),
            "obstacle": self._lookup(Obstacle),
            "weight_status": self._lookup(RaceWeightStatus),
        }

    def _lookup(self, enum: Type[Enum]) -> Enum | None:
        """Private method to lookup an enum value from a list of words

        :param enum: Enum to search through
        :type enum: Type[Enum]
        :return: The found Enum value or None
        :rtype: Enum | None
        """
        return next(
            (
                found_value
                for word in self._words
                if (found_value := getattr(enum, word, None)) is not None
            ),
            None,
        )
