import re

from horsetalk.quantity import HorsetalkQuantity


class RaceDistance(HorsetalkQuantity):
    """
    A convenience class for representing the distance over which a race is run.

    """

    REGEX = r"(?:(\d+)(?:m)\s*)?(?:(\d+)(?:f)\s*)?(?:(\d+)(?:y)\s*)?"

    def __str__(self) -> str:
        """
        Returns the distance as a string.
        """
        mile = self.furlong // 8
        furlong = (self.furlong % 8) // 1
        yard = (self.furlong % 1) * 220
        return " ".join(
            [
                f"{int(mile)}m" if mile else "",
                f"{int(furlong)}f" if furlong else "",
                f"{int(yard)}y" if yard else "",
            ]
        ).strip()

    @classmethod
    def _string_arg_handler(cls, arg):
        m, f, y = re.match(cls.REGEX, arg.replace(",", "")).groups()

        if int(m or 0) > 10:
            args = (int(m or 0), "metre")
        else:
            yards = int(m or 0) * 1760 + int(f or 0) * 220 + int(y or 0)
            args = (yards, "yard")

        return args