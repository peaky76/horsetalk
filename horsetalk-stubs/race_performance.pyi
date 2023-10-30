from _typeshed import Incomplete

from .disaster import Disaster as Disaster
from .finishing_position import FinishingPosition as FinishingPosition
from .horselength import Horselength as Horselength
from .outcome import Outcome as Outcome

class RacePerformance:
    comments: Incomplete
    outcome: Incomplete
    official_position: Incomplete
    beaten_distance: Incomplete
    def __init__(
        self,
        outcome: str | int | Disaster | FinishingPosition | Outcome,
        *,
        official_position: str | int | FinishingPosition | None = ...,
        beaten_distance: str | int | Horselength | None = ...,
        comments: str | None = ...
    ) -> None: ...
    @property
    def is_completion(self) -> bool: ...
    @property
    def is_official_win(self) -> bool: ...
    @property
    def is_win(self) -> bool: ...
