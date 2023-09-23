from typing import Self
from peak_utility.number import RepresentationalInt


class Draw(RepresentationalInt):
    def __new__(cls, value: int | str) -> None:
        """
        Create a Draw instance.

        Args:
            value: The stall number in which the horse is drawn.
        """
        if not str(int(value)) == str(value):
            raise ValueError("Draw must represent an integer value")

        return super().__new__(cls, value)

    def __add__(self, other: Self) -> bool:
        raise TypeError("Instances of draw cannot be added")

    def __sub__(self, other: Self) -> bool:
        raise TypeError("Instances of draw cannot be subtracted")

    def __mul__(self, other: Self) -> bool:
        raise TypeError("Instances of draw cannot be multiplied")

    def __truediv__(self, other: Self) -> bool:
        raise TypeError("Instances of draw cannot be divided")
