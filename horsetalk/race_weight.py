import re
from decimal import Decimal

from horsetalk._pint import Q_


class RaceWeight(Q_):
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
        elif not args:
            args = next(iter(kwargs.items()), None)[::-1]

        instance = Q_.__new__(Q_, *args)
        instance.__class__ = cls
        return instance

    def __repr__(self) -> str:
        """
        Returns the weight as a repr.
        """
        return f"<RaceWeight: {self!s}>"

    def __str__(self) -> str:
        """
        Returns the weight as a string.
        """
        num = self.to("lb").magnitude
        st, lb = divmod(num, 14)
        return f"{st}st {lb}lb"

    @property
    def kg(self) -> Decimal:
        return self.to("kg").magnitude

    @property
    def lb(self) -> Decimal:
        return self.to("lb").magnitude

    @property
    def st(self) -> Decimal:
        return self.to("st").magnitude
