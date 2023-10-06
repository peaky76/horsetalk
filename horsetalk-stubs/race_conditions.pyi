from .going import Going as Going
from .race_designation import RaceDesignation as RaceDesignation
from .race_distance import RaceDistance as RaceDistance
from .race_level import RaceLevel as RaceLevel
from .racecourse import Racecourse as Racecourse
from .stalls_position import StallsPosition as StallsPosition
from _typeshed import Incomplete
from pendulum import DateTime as DateTime

class RaceConditions:
    datetime: Incomplete
    racecourse: Incomplete
    distance: Incomplete
    going: Incomplete
    race_designation: Incomplete
    race_level: Incomplete
    stalls_position: Incomplete
    def __init__(self, *, datetime: DateTime, racecourse: Racecourse, distance: RaceDistance, going: Going, race_designation: RaceDesignation, race_level: RaceLevel, stalls_position: StallsPosition | None = ...) -> None: ...
