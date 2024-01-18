import re
from decimal import Decimal

from horsetalk.quantity import HorsetalkQuantity


class RaceDistance(HorsetalkQuantity):
    """
    A convenience class for representing the distance over which a race is run.

    """

    REGEX = r"(?:(\d+)(?:m)\s*)?(?:(\d+)(?:f)\s*)?(?:(\d+)(?:y)\s*)?"

    def __new__(cls, *args, **kwargs):
        """
        Initializes a RaceDistance object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A RaceDistance object.
        """
        if args and isinstance(args[0], str):
            if not re.fullmatch(r"(?:\d+[m|f|y]\s*)*", args[0].replace(",", "")):
                raise AttributeError(f"Invalid distance string: {args[0]}")

            m, f, y = re.match(RaceDistance.REGEX, args[0].replace(",", "")).groups()

            if int(m or 0) > 10:
                args = (int(m or 0), "metre")
            else:
                yards = int(m or 0) * 1760 + int(f or 0) * 220 + int(y or 0)
                args = (yards, "yard")

        return super().__new__(cls, *args, **kwargs)

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

    @property
    def furlong(self) -> Decimal:
        return self.to("furlong").magnitude

    @property
    def km(self) -> Decimal:
        return self.to("km").magnitude

    @property
    def metre(self) -> Decimal:
        return self.to("metre").magnitude

    @property
    def mile(self) -> Decimal:
        return self.to("mile").magnitude

    @property
    def yard(self) -> Decimal:
        return self.to("yard").magnitude

    @property
    def yd(self) -> Decimal:
        return self.to("yd").magnitude
