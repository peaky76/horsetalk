import re

from horsetalk.quantity import HorsetalkQuantity


class RaceWeight(HorsetalkQuantity):
    """
    A class for representing the weight carried by a horse in a race.

    """

    REGEX = r"(?:(\d+)(?:st|\-))?(?:(\d+)(?:lb)*)?"

    def __new__(cls, *args, **kwargs):
        """
        Initializes a RaceWeight object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A RaceWeight object.
        """
        if args and isinstance(args[0], str):
            st, lbs = re.match(RaceWeight.REGEX, args[0]).groups()
            args = (int(st or 0) * 14 + int(lbs or 0), "lb")

        return super().__new__(cls, *args, **kwargs)

    def __str__(self) -> str:
        """
        Returns the weight as a string.
        """
        num = self.to("lb").magnitude
        st, lb = divmod(num, 14)
        return f"{st}st {lb}lb"