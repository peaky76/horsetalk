from decimal import Decimal

from horsetalk._pint import Q_


class HorseHeight(Q_):
    """
    A class for measuring a horse's height.

    """

    def __new__(cls, *args, **kwargs):
        """
        Initializes a HorseHeight object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A HorseHeight object.
        """

        instance = Q_.__new__(Q_, *args, **kwargs)
        instance.__class__ = cls
        return instance

    def __repr__(self) -> str:
        """
        Returns:
            A representation of the HorseHeight object.
        """
        return f"<HorseHeight: {self!s}>"

    def __str__(self) -> str:
        """
        Returns:
            A string representation of the HorseHeight object.
        """
        return f"{self.to('hh').magnitude}hh"

    @property
    def hand(self) -> Decimal:
        """
        Returns the height in hands.
        """
        return self.to("hh").magnitude
