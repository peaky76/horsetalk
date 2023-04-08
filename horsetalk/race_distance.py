from decimal import Decimal
import re
from measurement.measures import Distance  # type: ignore


class RaceDistance(Distance):
    """
    A thin wrapper around the measurement library Distance class to allow for the creation of Distance objects
    from strings and to provide a way to initialize with furlongs.
    """

    def __init__(self, distance: str) -> None:
        """
        Initialize a RaceDistance object from a string.
        """
        pattern = re.compile(r"(\d+\D+)")
        unit_dict = {"m": "mile", "f": "furlong", "y": "yard"}
        vals_and_units = pattern.findall(distance.replace(" ", ""))

        distance = Distance(m=0)
        for vu in vals_and_units:
            val, unit = re.compile(r"(\d+)(\D+)").match(vu).groups()
            if unit_dict[unit] == "furlong":
                distance += Distance(chain=int(val) * 10)
            else:
                distance += Distance(**{unit_dict[unit]: int(val)})

        super().__init__(self, m=distance.m)

    @property
    def furlong(self) -> Decimal:
        """
        Returns the distance in furlongs.
        """
        return Decimal(self.chain / 10)
