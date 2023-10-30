from decimal import Decimal

from measurement.measures import Distance

class HorseHeight(Distance):
    def __init__(self, distance: str) -> None: ...
    @property
    def hand(self) -> Decimal: ...
