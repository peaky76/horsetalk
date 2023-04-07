from horsetalk import Obstacle, RaceAgeStatus


class RaceTitle:
    @staticmethod
    def parse(title: str):
        words = title.split()
        return {
            "age_status": (
                next(
                    (
                        found_value
                        for word in words
                        if (found_value := getattr(RaceAgeStatus, word, None))
                        is not None
                    ),
                    None,
                )
            ),
            "obstacle": (
                next(
                    (
                        found_value
                        for word in words
                        if (found_value := getattr(Obstacle, word, None)) is not None
                    ),
                    None,
                )
            ),
        }
