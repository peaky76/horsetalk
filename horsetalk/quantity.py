import re

from pint import UnitRegistry

ureg = UnitRegistry()
ureg.define("hand = 4 * inch = hh")
ureg.define("furlong = 0.125 * mile = f")
ureg.define("@alias yard = y")
Q_ = ureg.Quantity

class HorsetalkQuantity(Q_):

    REGEX = r"\d+\D+"

    def __new__(cls, *args, **kwargs):
        """
        Initializes a HorsetalkQuantity object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A HorsetalkQuantity object.
        """
        if args and isinstance(args[0], str):
            if not re.fullmatch(cls.REGEX, args[0].replace(",", "")):
                raise AttributeError(f"Invalid {cls.__name__.lower()} string: {args[0]}")
            args = cls._string_arg_handler(args[0])

        if not args:
            args = next(iter(kwargs.items()), None)[::-1]

        instance = Q_.__new__(Q_, *args)
        instance.__class__ = cls
        return instance

    def __repr__(self) -> str:
        """
        Returns:
            A representation of a HorsetalkQuantity object.
        """
        return f"<{self.__class__.__name__}: {self!s}>"

    def __getattr__(self, attr):
        return self.to(attr).magnitude

    @classmethod
    def _string_arg_handler(cls, arg):
        return [arg]