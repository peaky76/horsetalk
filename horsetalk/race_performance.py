from .disaster import Disaster
from peak_utility.number import Ordinal


class RacePerformance:
    """
    A class for grouping together race performance stats into a single object.

    """

    def __init__(
        self,
        outcome: str | int | Disaster,
        *,
        official_position: str | int | None = None,
        comments: str | None = None,
    ):
        """
        Initialize a RaceConditions instance.

        Args:
            datetime: The datetime of the race
            racecourse: The racecourse on which the race is run
            distance: The race distance
            going: The going of the race
            stalls_position: The position of the stalls on the track

        """
        self.comments = comments
        self.finishing_position = str(outcome) if str(outcome).isdigit() else None
        self.official_position = (
            str(official_position) if official_position else self.finishing_position
        )
        try:
            self.disaster = (
                None
                if self.finishing_position
                else Disaster[outcome]
                if isinstance(outcome, str)
                else outcome
            )
        except KeyError:
            raise ValueError(f"{outcome} is not a valid disaster")

        if self.disaster and self.official_position:
            raise ValueError(
                f"Cannot have both a disaster {self.disaster} and a position {self.official_position}"
            )

    def __repr__(self):
        official_position_repr = (
            f", placed {self.official_position}"
            if self.official_position != self.finishing_position
            else ""
        )
        return f"<RacePerformance: {self.disaster if self.disaster else self.finishing_position}{official_position_repr}>"

    def __str__(self):
        official_position_str = (
            f", placed {repr(Ordinal(self.official_position))}"
            if self.official_position != self.finishing_position
            else ""
        )
        return (
            f"{self.disaster.name.title()}"
            if self.disaster
            else f"{repr(Ordinal(self.finishing_position))}{official_position_str}"
        )
