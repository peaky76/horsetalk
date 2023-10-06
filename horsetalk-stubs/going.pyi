from .aw_going_description import AWGoingDescription as AWGoingDescription
from .dirt_going_description import DirtGoingDescription as DirtGoingDescription
from .going_description import GoingDescription as GoingDescription
from .turf_going_description import TurfGoingDescription as TurfGoingDescription
from _typeshed import Incomplete

class Going:
    Scales: Incomplete
    description: Incomplete
    reading: Incomplete
    def __init__(self, description: str, reading: float | None = ...) -> None: ...
    @property
    def primary(self) -> GoingDescription: ...
    @property
    def secondary(self) -> GoingDescription | None: ...
    @property
    def value(self) -> float: ...
