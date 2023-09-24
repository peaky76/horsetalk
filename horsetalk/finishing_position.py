from peak_utility.number import Ordinal  # type: ignore


class FinishingPosition(Ordinal):
    """
    A class that represents the finishing position of a horse in a race.

    """

    def __new__(cls, value, *, tied=False):
        if int(value) == 0:
            return int.__new__(cls, 0)

        instance = super().__new__(cls, value)
        instance.tied = tied
        return instance

    def __bool__(self):
        return int(self) >= 0

    def __repr__(self):
        if int(self) == 0:
            return "<FinishingPosition: Unplaced>"
        return f"<FinishingPosition: {'=' if self.tied else ''}{super().__repr__()}>"

    def __str__(self):
        if int(self) == 0:
            return "Unplaced"
        return f"{'=' if self.tied else ''}{super().__repr__()}"
