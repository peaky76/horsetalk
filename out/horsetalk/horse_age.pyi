from pendulum import DateTime as DateTime, Interval as Interval
from typing import Self

class HorseAge:
    def __init__(self, official_age: int | None = None, *, foaling_date: DateTime | None = None, birth_year: int | None = None, context_date: DateTime | None = None) -> None: ...
    @property
    def official(self) -> Interval: ...
    @property
    def actual(self) -> Interval: ...
    @property
    def date_of_birth(self) -> DateTime: ...
    @property
    def year_of_birth(self) -> int: ...
    def at(self, date: DateTime) -> Self: ...
