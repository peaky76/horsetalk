from enum import Enum
from typing import List
from horsetalk import Obstacle, RaceAgeStatus, RaceExperienceStatus


class RaceTitle:
    _words = []

    @classmethod
    def parse(cls, title: str):
        self = cls()
        self._words = title.split()
        return {
            "age_status": self._lookup(RaceAgeStatus),
            "experience_status": self._lookup(RaceExperienceStatus),
            "obstacle": self._lookup(Obstacle),
        }

    def _lookup(self, enum: Enum):
        return next(
            (
                found_value
                for word in self._words
                if (found_value := getattr(enum, word, None)) is not None
            ),
            None,
        )
