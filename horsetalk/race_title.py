from enum import Enum
from typing import List
from horsetalk import Obstacle, RaceAgeStatus, RaceExperienceStatus


class RaceTitle:
    @staticmethod
    def parse(title: str):
        words = title.split()
        return {
            "age_status": RaceTitle._lookup(words, RaceAgeStatus),
            "experience_status": RaceTitle._lookup(words, RaceExperienceStatus),
            "obstacle": RaceTitle._lookup(words, Obstacle),
        }

    @staticmethod
    def _lookup(words: List[str], enum: Enum):
        return next(
            (
                found_value
                for word in words
                if (found_value := getattr(enum, word, None)) is not None
            ),
            None,
        )
