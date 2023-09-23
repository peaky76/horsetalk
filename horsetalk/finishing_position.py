from peak_utility.number import Ordinal  # type: ignore


class FinishingPosition(Ordinal):
    """
    A class that represents the finishing position of a horse in a race.

    """

    def __new__(cls, value):
        if int(value) < 0:
            raise ValueError("Finishing position cannot be negative.")

        if int(value) == 0:
            return int.__new__(cls, 0)

        return super().__new__(cls, value)

    def __bool__(self):
        return int(self) >= 0

    def __repr__(self):
        if int(self) == 0:
            return "<FinishingPosition: Unplaced>"
        return f"<FinishingPosition: {super().__repr__()}>"

    def __str__(self):
        if int(self) == 0:
            return "Unplaced"
        return super().__repr__()
