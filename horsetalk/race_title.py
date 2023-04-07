from horsetalk.obstacle import Obstacle


class RaceTitle:
    @staticmethod
    def parse(title: str):
        words = title.split()
        return {
            "obstacle": (
                next(
                    (
                        found_value
                        for word in words
                        if (found_value := getattr(Obstacle, word, None)) is not None
                    ),
                    None,
                )
            )
        }
