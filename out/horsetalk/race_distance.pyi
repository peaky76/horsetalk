from decimal import Decimal
from measurement.measures import Distance

class RaceDistance(Distance):
    def __init__(self, distance: str) -> None: ...
    @property
    def furlong(self) -> Decimal: ...
