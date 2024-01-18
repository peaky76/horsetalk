from pint import UnitRegistry

ureg = UnitRegistry()
ureg.define("hand = 4 * inch = hh")
ureg.define("furlong = 0.125 * mile = f")
ureg.define("@alias yard = y")
Q_ = ureg.Quantity

class HorsetalkQuantity(Q_):

    def __new__(cls, *args, **kwargs):
        """
        Initializes a HorsetalkQuantity object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A HorsetalkQuantity object.
        """

        instance = Q_.__new__(Q_, *args, **kwargs)
        instance.__class__ = cls
        return instance

    def __repr__(self) -> str:
        """
        Returns:
            A representation of a HorsetalkQuantity object.
        """
        return f"<{self.__class__.__name__}: {self!s}>"