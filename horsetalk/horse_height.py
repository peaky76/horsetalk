from decimal import Decimal

from horsetalk.quantity import HorsetalkQuantity


class HorseHeight(HorsetalkQuantity):
    """
    A class for measuring a horse's height.

    """

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
