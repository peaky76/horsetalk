from enum import Enum
from .obstacle import Obstacle
from .race_age_status import RaceAgeStatus
from .race_experience_status import RaceExperienceStatus
from .race_weight_status import RaceWeightStatus


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
            "weight_status": self._lookup(RaceWeightStatus),
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
