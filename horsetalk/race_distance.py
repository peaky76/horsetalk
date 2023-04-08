from decimal import Decimal
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
        if "m" in distance:
            parts = distance.split("m")
            miles = int(parts[0])
            furlongs = int(parts[1].split("f")[0] if len(parts) > 1 and parts[1] else 0)
        else:
            parts = distance.split("f")
            miles = 0
            furlongs = int(parts[0]) if "f" in distance else 0
        super().__init__(self, chain=((miles * 8) + furlongs) * 10)

    @property
    def furlong(self) -> Decimal:
        """
        Returns the distance in furlongs.
        """
        return Decimal(self.chain / 10)
